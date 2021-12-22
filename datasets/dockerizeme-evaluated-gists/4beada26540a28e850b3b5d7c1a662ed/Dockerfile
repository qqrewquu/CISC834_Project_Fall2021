FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4beada26540a28e850b3b5d7c1a662ed/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
