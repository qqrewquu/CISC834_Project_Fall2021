from django import template
from django.template import Context
from django.template.base import parse_bits

from wagtail.wagtailimages.templatetags.wagtailimages_tags import ImageNode
from wagtail.wagtailimages.models import Filter, SourceImageIOError, InvalidFilterSpecError

from britishswimming.utils.models import SocialMediaSettings

register = template.Library()

@register.tag(name="responsiveimage")
def responsiveimage(parser, token):
    bits = token.split_contents()[1:]
    image_expr = parser.compile_filter(bits[0])
    filter_spec = bits[1]
    remaining_bits = bits[2:]

    attrs = {}

    if remaining_bits[-2:][0] == 'as':
        for bit in remaining_bits[:-2]:
            try:
                name, value = bit.split('=')
            except ValueError:
                raise template.TemplateSyntaxError("'responsiveimage' tag should be of the form {% responsiveimage self.photo max-320x200 srcset=\"whatever\" [ custom-attr=\"value\" ... ] %} or {% responsiveimage self.photo max-320x200 srcset=\"whatever\" as img %}")
            attrs[name] = parser.compile_filter(value) # setup to resolve context variables as value

        # token is of the form {% responsiveimage self.photo max-320x200 srcset="whatever" as img %}
        return ResponsiveImageNode(image_expr, filter_spec, attrs=attrs, output_var_name=remaining_bits[-2:][1])
    else:
        # token is of the form {% responsiveimage self.photo max-320x200 srcset="whatever" %} - all additional tokens
        # should be kwargs, which become attributes
        for bit in remaining_bits:
            try:
                name, value = bit.split('=')
            except ValueError:
                raise template.TemplateSyntaxError("'responsiveimage' tag should be of the form {% responsiveimage self.photo max-320x200 srcset=\"whatever\" [ custom-attr=\"value\" ... ] %} or {% responsiveimage self.photo max-320x200 srcset=\"whatever\" as img %}")

            attrs[name] = parser.compile_filter(value) # setup to resolve context variables as value

        return ResponsiveImageNode(image_expr, filter_spec, attrs=attrs)

class ResponsiveImageNode(ImageNode, template.Node):
    def render(self, context):
        try:
            image = self.image_expr.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        if not image:
            return ''

        try:
            rendition = image.get_rendition(self.filter)
        except SourceImageIOError:
            # It's fairly routine for people to pull down remote databases to their
            # local dev versions without retrieving the corresponding image files.
            # In such a case, we would get a SourceImageIOError at the point where we try to
            # create the resized version of a non-existent image. Since this is a
            # bit catastrophic for a missing image, we'll substitute a dummy
            # Rendition object so that we just output a broken link instead.
            Rendition = image.renditions.model  # pick up any custom Image / Rendition classes that may be in use
            rendition = Rendition(image=image, width=0, height=0)
            rendition.file.name = 'not-found'


        # Parse srcset format into array
        try:
            raw_sources = str(self.attrs['srcset']).replace('"', '').split(',')

            srcset_renditions = []
            widths = []
            newsrcseturls = []

            for source in raw_sources:
                flt = source.strip().split(' ')[0]
                width = source.strip().split(' ')[1]

                # cache widths to be re-appended after filter has been converted to URL
                widths.append(width)

                try:
                    srcset_renditions.append(image.get_rendition(flt))
                except SourceImageIOError:
                    TmpRendition = image.renditions.model  # pick up any custom Image / Rendition classes that may be in use
                    tmprend = TmpRendition(image=image, width=0, height=0)
                    tmprend.file.name = 'not-found'

            for index, rend in enumerate(srcset_renditions):
                newsrcseturls.append(' '.join([rend.url, widths[index]]))

        except KeyError:
            newsrcseturls = []
            pass

        if self.output_var_name:
            rendition.srcset = ', '.join(newsrcseturls)

            # return the rendition object in the given variable
            context[self.output_var_name] = rendition
            return ''
        else:
            # render the rendition's image tag now
            resolved_attrs = {}
            for key in self.attrs:
                if key == 'srcset':
                    resolved_attrs[key] = ','.join(newsrcseturls)
                    continue

                resolved_attrs[key] = self.attrs[key].resolve(context)

            return rendition.img_tag(resolved_attrs)
