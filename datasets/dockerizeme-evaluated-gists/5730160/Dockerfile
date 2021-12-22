FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5730160/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
