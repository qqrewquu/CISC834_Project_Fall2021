FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5091799/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","python"]
RUN ["pip","install","tornado"]
RUN ["pip","install","pika"]
CMD ["python","/snippet.py"]
