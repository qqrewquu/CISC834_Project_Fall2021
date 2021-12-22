FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7986974/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","cql"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-tagging"]
RUN ["apt-get","install","-y","python-cairo"]
RUN ["pip","install","whisper"]
CMD ["python","/snippet.py"]
