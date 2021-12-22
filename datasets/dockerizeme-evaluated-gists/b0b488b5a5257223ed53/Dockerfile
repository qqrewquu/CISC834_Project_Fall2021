FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b0b488b5a5257223ed53/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
