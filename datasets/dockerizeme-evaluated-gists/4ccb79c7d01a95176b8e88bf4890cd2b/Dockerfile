FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4ccb79c7d01a95176b8e88bf4890cd2b/snippet.py /snippet.py
RUN ["pip","install","plex.py"]
RUN ["pip","install","PlexAPI"]
CMD ["python","/snippet.py"]
