FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4188305/snippet.py /snippet.py
RUN ["pip","install","bson"]
RUN ["pip","install","Flask"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
