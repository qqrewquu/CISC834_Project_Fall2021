FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3880042/snippet.py /snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","tweepy"]
RUN ["pip","install","redis"]
CMD ["python","/snippet.py"]
