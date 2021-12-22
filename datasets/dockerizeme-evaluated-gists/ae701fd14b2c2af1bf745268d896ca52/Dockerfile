FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ae701fd14b2c2af1bf745268d896ca52/snippet.py /snippet.py
RUN ["pip","install","pwntools"]
RUN ["pip","install","pwn"]
CMD ["python","/snippet.py"]
