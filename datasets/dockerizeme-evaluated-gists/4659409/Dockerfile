FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4659409/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","requests"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
