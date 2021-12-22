FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5183375/snippet.py /snippet.py
RUN ["pip","install","tweepy"]
RUN ["pip","install","nltk"]
RUN ["pip","install","Haiku"]
CMD ["python","/snippet.py"]
