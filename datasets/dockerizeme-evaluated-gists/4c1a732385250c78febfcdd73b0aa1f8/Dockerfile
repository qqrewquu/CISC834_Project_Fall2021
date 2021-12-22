FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4c1a732385250c78febfcdd73b0aa1f8/snippet.py /snippet.py
RUN ["pip","install","tweepy"]
CMD ["python","/snippet.py"]
