FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/682979133e732c4cd3ab9467e5c70273/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","music21"]
CMD ["python","/snippet.py"]
