FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b1d8c07b96a8fecb319c7902773f9c0a/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
