FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7bb75a8f280f501344b8/snippet.py /snippet.py
RUN ["pip","install","trans"]
RUN ["pip","install","transmissionrpc"]
CMD ["python","/snippet.py"]
