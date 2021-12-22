FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/11005158/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","mongo"]
RUN ["pip","install","bson"]
RUN ["pip","install","pymongo"]
RUN ["pip","install","Flask-JSON"]
CMD ["python","/snippet.py"]
