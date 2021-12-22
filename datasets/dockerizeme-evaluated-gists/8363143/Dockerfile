FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8363143/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","requests"]
RUN ["pip","install","simple-salesforce"]
RUN ["pip","install","simpl"]
CMD ["python","/snippet.py"]
