FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1b4475f214cf246e246ee3e7d143d843/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","toml"]
RUN ["pip","install","pandas"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
