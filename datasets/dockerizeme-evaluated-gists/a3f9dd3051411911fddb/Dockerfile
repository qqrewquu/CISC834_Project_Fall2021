FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a3f9dd3051411911fddb/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
