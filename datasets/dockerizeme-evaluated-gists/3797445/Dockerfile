FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3797445/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
CMD ["python","/snippet.py"]
