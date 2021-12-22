FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7500554/snippet.py /snippet.py
RUN ["pip","install","musicbrainzngs"]
CMD ["python","/snippet.py"]
