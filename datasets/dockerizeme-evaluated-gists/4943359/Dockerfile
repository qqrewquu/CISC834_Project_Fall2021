FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4943359/snippet.py /snippet.py
RUN ["pip","install","param"]
RUN ["pip","install","paramiko"]
CMD ["python","/snippet.py"]
