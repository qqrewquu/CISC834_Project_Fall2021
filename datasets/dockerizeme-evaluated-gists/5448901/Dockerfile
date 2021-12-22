FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5448901/snippet.py /snippet.py
RUN ["pip","install","nltk"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
