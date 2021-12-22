FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2d8566cbd500cc738cb20461751bec8e/snippet.py /snippet.py
RUN ["pip","install","pwntools"]
RUN ["pip","install","pwn"]
CMD ["python","/snippet.py"]
