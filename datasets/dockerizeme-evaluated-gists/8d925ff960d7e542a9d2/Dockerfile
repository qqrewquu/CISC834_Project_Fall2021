FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8d925ff960d7e542a9d2/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","chai"]
RUN ["pip","install","chainer"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
