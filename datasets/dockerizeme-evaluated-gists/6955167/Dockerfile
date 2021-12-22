FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6955167/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","fabulous"]
CMD ["python","/snippet.py"]
