FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3fabf65987f4bd2dea37/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","docutils"]
RUN ["pip","install","pydocumentdb"]
CMD ["python","/snippet.py"]
