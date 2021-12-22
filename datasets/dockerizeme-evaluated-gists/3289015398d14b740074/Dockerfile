FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3289015398d14b740074/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","alembic"]
CMD ["python","/snippet.py"]
