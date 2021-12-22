FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8eeb01a5e0db704521fa37b125c2861e/snippet.py /snippet.py
RUN ["pip","install","chai"]
RUN ["pip","install","chainer"]
CMD ["python","/snippet.py"]
