FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1d2577af55c8320ffd6a/snippet.py /snippet.py
RUN ["pip","install","param"]
RUN ["pip","install","paramiko"]
CMD ["python","/snippet.py"]
