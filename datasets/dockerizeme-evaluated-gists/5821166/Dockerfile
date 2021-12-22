FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5821166/snippet.py /snippet.py
RUN ["pip","install","nltk"]
RUN ["pip","install","networkx"]
CMD ["python","/snippet.py"]
