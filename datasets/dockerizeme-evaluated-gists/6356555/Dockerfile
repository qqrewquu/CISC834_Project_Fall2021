FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6356555/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simplejson"]
RUN ["pip","install","pickleDB"]
RUN ["pip","install","simpl"]
CMD ["python","/snippet.py"]
