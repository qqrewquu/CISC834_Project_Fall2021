FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7432419/snippet.py /snippet.py
RUN ["pip","install","python-louvain"]
RUN ["pip","install","networkx"]
RUN ["pip","install","androidviewclient"]
RUN ["pip","install","community"]
CMD ["python","/snippet.py"]
