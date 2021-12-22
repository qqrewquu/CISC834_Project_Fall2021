FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7d9f439a6eb16dee7fee/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","tweepy"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
