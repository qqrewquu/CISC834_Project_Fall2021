FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4af649ff88612b2de7c7/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","oauthlib"]
CMD ["python","/snippet.py"]
