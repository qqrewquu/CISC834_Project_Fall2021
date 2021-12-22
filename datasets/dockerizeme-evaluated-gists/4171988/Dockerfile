FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4171988/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
