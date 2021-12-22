FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4707291/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytz"]
RUN ["pip","install","mutagen"]
CMD ["python","/snippet.py"]
