FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9262225/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
