FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b0aa5cbfa42f4eb23eb9/snippet.py /snippet.py
RUN ["pip","install","bit"]
RUN ["pip","install","bitarray"]
CMD ["python","/snippet.py"]
