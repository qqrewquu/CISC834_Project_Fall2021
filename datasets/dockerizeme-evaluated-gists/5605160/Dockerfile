FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5605160/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","docopt"]
RUN ["pip","install","konch"]
RUN ["pip","install","pydocumentdb"]
CMD ["python","/snippet.py"]
