FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5050915/snippet.py /snippet.py
RUN ["pip","install","IMAPClient"]
CMD ["python","/snippet.py"]
