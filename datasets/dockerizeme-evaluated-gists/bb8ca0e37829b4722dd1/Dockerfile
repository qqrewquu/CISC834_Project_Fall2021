FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bb8ca0e37829b4722dd1/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","logging-config"]
RUN ["pip","install","alembic"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
