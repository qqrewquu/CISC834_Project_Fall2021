FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7a4989490300d1298ba0/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Flask-SQLAlchemy"]
RUN ["pip","install","Flask-SQLAlchemy-Meiqia"]
RUN ["pip","install","Flask-SQLAlchemy-tw"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
