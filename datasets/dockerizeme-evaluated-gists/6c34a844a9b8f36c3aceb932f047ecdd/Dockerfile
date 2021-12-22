FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6c34a844a9b8f36c3aceb932f047ecdd/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
