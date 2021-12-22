FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6757242/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","docopt"]
RUN ["pip","install","bucket3"]
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","Unidecode"]
RUN ["pip","install","konch"]
CMD ["python","/snippet.py"]
