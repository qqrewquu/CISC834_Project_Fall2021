FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b77f6d62a595ae329e41/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-mws"]
CMD ["python","/snippet.py"]
