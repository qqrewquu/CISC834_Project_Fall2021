FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6caa622be083f97b8c5c9a10478ba058/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pycorenlp"]
CMD ["python","/snippet.py"]
