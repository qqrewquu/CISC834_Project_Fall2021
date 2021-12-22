FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8051599/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
