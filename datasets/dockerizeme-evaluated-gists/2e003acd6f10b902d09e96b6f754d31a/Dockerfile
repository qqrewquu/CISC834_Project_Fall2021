FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2e003acd6f10b902d09e96b6f754d31a/snippet.py /snippet.py
RUN ["pip","install","scapy-python3"]
RUN ["pip","install","pefile"]
RUN ["pip","install","scapy-http"]
CMD ["python","/snippet.py"]
