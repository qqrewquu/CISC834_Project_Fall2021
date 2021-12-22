FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8bdb1092579041ce739c/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","networkx"]
CMD ["python","/snippet.py"]
