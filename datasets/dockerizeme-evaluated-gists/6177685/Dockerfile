FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6177685/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","tweepy"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
