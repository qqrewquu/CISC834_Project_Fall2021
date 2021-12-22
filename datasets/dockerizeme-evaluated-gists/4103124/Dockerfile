FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4103124/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Inject"]
RUN ["pip","install","injector"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
