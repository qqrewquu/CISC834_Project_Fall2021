FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6166111/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","pytz"]
RUN ["pip","install","mutagen"]
CMD ["python","/snippet.py"]
