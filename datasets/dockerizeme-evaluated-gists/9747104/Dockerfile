FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9747104/snippet.py /snippet.py
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","vobject"]
CMD ["python","/snippet.py"]
