FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9561148/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","flask-peewee"]
RUN ["pip","install","psycopg2"]
CMD ["python","/snippet.py"]
