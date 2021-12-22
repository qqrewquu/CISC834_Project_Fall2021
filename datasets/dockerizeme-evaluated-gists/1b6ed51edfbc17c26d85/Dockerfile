FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1b6ed51edfbc17c26d85/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pandas"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
