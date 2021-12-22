FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8982799/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","dropbox"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
