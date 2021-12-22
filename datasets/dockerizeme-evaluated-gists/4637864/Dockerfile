FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4637864/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
CMD ["python","/snippet.py"]
