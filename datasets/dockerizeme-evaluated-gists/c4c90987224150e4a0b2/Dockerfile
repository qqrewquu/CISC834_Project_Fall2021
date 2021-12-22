FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c4c90987224150e4a0b2/snippet.py /snippet.py
RUN ["pip","install","pyd"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","PyDrive"]
CMD ["python","/snippet.py"]
