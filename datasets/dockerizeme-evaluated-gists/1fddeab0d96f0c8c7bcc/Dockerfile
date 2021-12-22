FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1fddeab0d96f0c8c7bcc/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
CMD ["python","/snippet.py"]
