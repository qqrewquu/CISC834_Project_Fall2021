FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5350769/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","konch"]
RUN ["pip","install","pydocumentdb"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","docopt"]
CMD ["python","/snippet.py"]
