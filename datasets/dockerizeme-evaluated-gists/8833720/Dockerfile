FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8833720/snippet.py /snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","simpl"]
RUN ["pip","install","shodan"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
