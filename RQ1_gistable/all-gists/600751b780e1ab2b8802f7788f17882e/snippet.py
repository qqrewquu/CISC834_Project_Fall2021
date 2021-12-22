from keras import layers
from keras import models
import tensorflow as tf


#
# generator input params
#

rand_dim = (1, 1, 2048)  # dimension of the generator's input tensor (gaussian noise)

#
# image dimensions
#

img_height = 224
img_width = 224
img_channels = 3

#
# shared network params
#

cardinality = 1


def add_common_layers(y):
    # batch norm is commented out b/c of keras bugs
    # y = layers.BatchNormalization()(y)
    y = layers.LeakyReLU()(y)

    return y


def grouped_convolution(y, nb_channels, _strides, _transposed=False):
    # when `cardinality` == 1 this is just a standard convolution
    if cardinality == 1:
        if _strides != (1, 1) and _transposed:
            return layers.Conv2DTranspose(nb_channels, kernel_size=(3, 3), strides=_strides, padding='same')(y)
        else:
            return layers.Conv2D(nb_channels, kernel_size=(3, 3), strides=_strides, padding='same')(y)

    assert not nb_channels % cardinality
    _d = nb_channels // cardinality

    # in a grouped convolution layer, input and output channels are divided into `cardinality` groups,
    # and convolutions are separately performed within each group
    groups = []
    for j in range(cardinality):
        group = layers.Lambda(lambda z: z[:, :, :, j * _d:j * _d + _d])(y)
        if _strides != (1, 1) and _transposed:
            groups.append(layers.Conv2DTranspose(_d, kernel_size=(3, 3), strides=_strides, padding='same')(group))
        else:
            groups.append(layers.Conv2D(_d, kernel_size=(3, 3), strides=_strides, padding='same')(group))

    # the grouped convolutional layer concatenates them as the outputs of the layer
    y = layers.concatenate(groups)

    return y


def residual_block(y, nb_channels_in, nb_channels_out, _strides=(1, 1), _project_shortcut=False, _transposed=False):
    """
    Our network consists of a stack of residual blocks. These blocks have the same topology,
    and are subject to two simple rules:
    - If producing spatial maps of the same size, the blocks share the same hyper-parameters (width and filter sizes).
    - Each time the spatial map is down-sampled by a factor of 2, the width of the blocks is multiplied by a factor of 2.
      * If up-sampled in case of `_transposed` == True, the width of the blocks is divided by a factor of 2.
    
    """
    shortcut = y

    # we modify the residual building block as a bottleneck design to make the network more economical
    y = layers.Conv2D(nb_channels_in, kernel_size=(1, 1), strides=(1, 1), padding='same')(y)
    y = add_common_layers(y)

    # ResNeXt (identical to ResNet when `cardinality` == 1)
    y = grouped_convolution(y, nb_channels_in, _strides=_strides, _transposed=_transposed)
    y = add_common_layers(y)

    y = layers.Conv2D(nb_channels_out, kernel_size=(1, 1), strides=(1, 1), padding='same')(y)
    # batch normalization is employed after aggregating the transformations and before adding to the shortcut
    # y = layers.BatchNormalization()(y)

    # identity shortcuts used directly when the input and output are of the same dimensions
    if _project_shortcut or _strides != (1, 1):
        # when the dimensions increase projection shortcut is used to match dimensions (done by 1×1 convolutions)
        # when the shortcuts go across feature maps of two sizes, they are performed with a stride of 2
        if _strides != (1, 1) and _transposed:
            shortcut = layers.Conv2DTranspose(nb_channels_out, kernel_size=(1, 1), strides=_strides, padding='same')(shortcut)
        else:
            shortcut = layers.Conv2D(nb_channels_out, kernel_size=(1, 1), strides=_strides, padding='same')(shortcut)

        # shortcut = layers.BatchNormalization()(shortcut)

    y = layers.add([shortcut, y])

    # relu is performed right after each batch normalization,
    # expect for the output of the block where relu is performed after the adding to the shortcut
    y = layers.LeakyReLU()(y)

    return y


def stack_blocks(x, transposed=False):
    # conv2
    for i in range(2):
        strides = (2, 2) if i == 0 else (1, 1)
        x = residual_block(x, 64, 256, _strides=strides, _transposed=transposed)

    # conv3
    for i in range(2):
        # down-sampling is performed by conv3_1, conv4_1, and conv5_1 with a stride of 2
        strides = (2, 2) if i == 0 else (1, 1)
        x = residual_block(x, 128, 512, _strides=strides, _transposed=transposed)

    # conv4
    for i in range(2):
        strides = (2, 2) if i == 0 else (1, 1)
        x = residual_block(x, 256, 1024, _strides=strides, _transposed=transposed)

    # conv5
    for i in range(2):
        strides = (2, 2) if i == 0 else (1, 1)
        x = residual_block(x, 512, 2048, _strides=strides, _transposed=transposed)

    return x


def generator_network(x):
    x = layers.Dense(64 * 7 * 7)(x)
    x = add_common_layers(x)

    x = layers.Reshape((7, 7, 64))(x)
    x = stack_blocks(x, transposed=True)

    # (conv1 disc)
    # number of feature maps => number of image channels
    return layers.Conv2DTranspose(img_channels, kernel_size=(7, 7), strides=(2, 2), padding='same', activation='tanh')(x)


def discriminator_network(x):
    """
    ResNeXt by default. For ResNet set `cardinality` = 1 above.
    
    """
    # conv1
    x = layers.Conv2D(64, kernel_size=(7, 7), strides=(2, 2), padding='same')(x)
    x = add_common_layers(x)

    x = stack_blocks(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(1)(x)

    return x
  

#
# define model input and output tensors
#

generator_input_tensor = layers.Input(shape=rand_dim)
generated_image_tensor = generator_network(generator_input_tensor)

generated_or_real_image_tensor = layers.Input(shape=(img_height, img_width, img_channels))
discriminator_output = discriminator_network(generated_or_real_image_tensor)

#
# define models
#

generator_model = models.Model(inputs=[generator_input_tensor], outputs=[generated_image_tensor], name='generator')
discriminator_model = models.Model(inputs=[generated_or_real_image_tensor],
                                   outputs=[discriminator_output],
                                   name='discriminator')

combined_output = discriminator_model(generator_model(generator_input_tensor))
combined_model = models.Model(inputs=[generator_input_tensor], outputs=[combined_output], name='combined')

print(generator_model.summary())
print(discriminator_model.summary())
print(combined_model.summary())
