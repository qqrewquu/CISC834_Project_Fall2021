FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bfe8b20c80e6f09c7105/snippet.py /snippet.py
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","seria"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
