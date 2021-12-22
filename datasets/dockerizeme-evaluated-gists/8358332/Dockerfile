FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8358332/snippet.py /snippet.py
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","six"]
RUN ["pip","install","docutils"]
RUN ["pip","install","pelican"]
CMD ["python","/snippet.py"]
