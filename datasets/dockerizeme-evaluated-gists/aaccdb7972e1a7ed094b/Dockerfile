FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/aaccdb7972e1a7ed094b/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","sqlalchemy-orm"]
CMD ["python","/snippet.py"]
