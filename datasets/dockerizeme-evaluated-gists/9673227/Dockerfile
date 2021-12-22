FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9673227/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
