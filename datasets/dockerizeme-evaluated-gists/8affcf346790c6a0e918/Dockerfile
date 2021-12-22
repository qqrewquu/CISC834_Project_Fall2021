FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8affcf346790c6a0e918/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","simple-salesforce"]
CMD ["python","/snippet.py"]
