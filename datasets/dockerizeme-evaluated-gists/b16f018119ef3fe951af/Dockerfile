FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b16f018119ef3fe951af/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","konch"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","docopt"]
RUN ["pip","install","pydocumentdb"]
CMD ["python","/snippet.py"]
