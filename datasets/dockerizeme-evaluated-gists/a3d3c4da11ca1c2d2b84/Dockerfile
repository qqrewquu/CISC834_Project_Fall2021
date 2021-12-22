FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a3d3c4da11ca1c2d2b84/snippet.py /snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","serial"]
CMD ["python","/snippet.py"]
