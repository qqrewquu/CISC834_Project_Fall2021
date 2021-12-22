FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bda10fa55df5723e27da/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","sqlalchemy-orm"]
CMD ["python","/snippet.py"]
