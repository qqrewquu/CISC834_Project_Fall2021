FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4721073/snippet.py /snippet.py
RUN ["pip","install","alembic"]
RUN ["pip","install","logging-config"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","wakatime"]
CMD ["python","/snippet.py"]
