FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0ef13930d561e42b9b213cadecfcf7c9/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-auth"]
CMD ["python","/snippet.py"]
