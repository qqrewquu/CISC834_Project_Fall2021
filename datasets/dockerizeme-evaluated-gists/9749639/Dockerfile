FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9749639/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","requests-auth"]
CMD ["python","/snippet.py"]
