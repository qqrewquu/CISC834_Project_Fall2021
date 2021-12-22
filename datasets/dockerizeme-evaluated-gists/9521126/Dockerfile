FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9521126/snippet.py /snippet.py
RUN ["pip","install","pycrypto"]
RUN ["pip","install","ecdsa"]
CMD ["python","/snippet.py"]
