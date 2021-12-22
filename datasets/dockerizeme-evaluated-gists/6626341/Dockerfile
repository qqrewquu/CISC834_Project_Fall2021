FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6626341/snippet.py /snippet.py
RUN ["pip","install","nltk"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
