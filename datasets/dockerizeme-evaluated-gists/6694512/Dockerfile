FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6694512/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
