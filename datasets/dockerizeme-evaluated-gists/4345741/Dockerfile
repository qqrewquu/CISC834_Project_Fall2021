FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4345741/snippet.py /snippet.py
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","sqlalchemy-orm"]
CMD ["python","/snippet.py"]
