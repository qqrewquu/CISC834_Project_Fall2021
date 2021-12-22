FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5263501/snippet.py /snippet.py
RUN ["pip","install","simpl"]
RUN ["pip","install","tweepy"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
