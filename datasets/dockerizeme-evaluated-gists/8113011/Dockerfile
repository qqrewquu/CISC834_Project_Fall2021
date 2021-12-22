FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8113011/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyes-fatisar"]
RUN ["pip","install","pyes"]
RUN ["pip","install","psycopg2"]
CMD ["python","/snippet.py"]
