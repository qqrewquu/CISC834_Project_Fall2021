FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bc8649d647240ef14311/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","serial"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
