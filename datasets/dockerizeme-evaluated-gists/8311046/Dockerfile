FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8311046/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","dropbox"]
CMD ["python","/snippet.py"]
