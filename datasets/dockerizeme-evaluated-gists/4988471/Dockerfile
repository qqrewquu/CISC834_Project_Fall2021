FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4988471/snippet.py /snippet.py
RUN ["pip","install","di-py"]
RUN ["pip","install","distlib"]
CMD ["python","/snippet.py"]
