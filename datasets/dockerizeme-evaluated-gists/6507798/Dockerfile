FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6507798/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","Flask-JSON"]
CMD ["python","/snippet.py"]
