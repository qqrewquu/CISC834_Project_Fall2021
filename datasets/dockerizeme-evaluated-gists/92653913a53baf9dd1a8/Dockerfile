FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/92653913a53baf9dd1a8/snippet.py /snippet.py
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","seria"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
