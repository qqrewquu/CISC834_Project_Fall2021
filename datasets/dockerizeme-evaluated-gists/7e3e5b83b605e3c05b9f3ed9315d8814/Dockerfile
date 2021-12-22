FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7e3e5b83b605e3c05b9f3ed9315d8814/snippet.py /snippet.py
RUN ["pip","install","pwntools"]
RUN ["pip","install","pwn"]
CMD ["python","/snippet.py"]
