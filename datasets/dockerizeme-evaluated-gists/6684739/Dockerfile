FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6684739/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pycares"]
CMD ["python","/snippet.py"]
