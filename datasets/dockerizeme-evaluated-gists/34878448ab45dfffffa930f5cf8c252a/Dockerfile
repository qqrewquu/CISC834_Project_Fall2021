FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/34878448ab45dfffffa930f5cf8c252a/snippet.py /snippet.py
RUN ["pip","install","plex.py"]
RUN ["pip","install","PlexAPI"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
