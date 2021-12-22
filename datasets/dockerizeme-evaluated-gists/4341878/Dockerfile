FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4341878/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
