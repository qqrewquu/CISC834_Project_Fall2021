FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3a39c61d11f3cacf4e58/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
CMD ["python","/snippet.py"]
