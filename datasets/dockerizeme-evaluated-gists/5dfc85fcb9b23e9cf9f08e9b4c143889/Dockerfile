FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5dfc85fcb9b23e9cf9f08e9b4c143889/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
