FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4963950/snippet.py /snippet.py
RUN ["pip","install","msgpack-python"]
RUN ["pip","install","msgpack"]
CMD ["python","/snippet.py"]
