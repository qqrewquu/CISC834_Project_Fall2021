FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b1aa2c0f604ed92b9b3afaa6db18e5fd/snippet.py /snippet.py
RUN ["pip","install","PlexAPI"]
RUN ["pip","install","plex.py"]
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
