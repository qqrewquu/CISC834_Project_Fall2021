FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3862093af36a1aeb8104/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
