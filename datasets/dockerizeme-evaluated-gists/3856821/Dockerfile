FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3856821/snippet.py /snippet.py
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","six"]
RUN ["pip","install","docutils"]
CMD ["python","/snippet.py"]
