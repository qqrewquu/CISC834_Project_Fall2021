FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a6c9b5119d418a65d489/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
