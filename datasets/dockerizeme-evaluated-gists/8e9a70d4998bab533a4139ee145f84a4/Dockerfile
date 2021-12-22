FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8e9a70d4998bab533a4139ee145f84a4/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytz"]
RUN ["pip","install","mutagen"]
CMD ["python","/snippet.py"]
