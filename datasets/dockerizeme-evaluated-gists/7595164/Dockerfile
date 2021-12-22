FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7595164/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pycoin"]
RUN ["pip","install","base58"]
CMD ["python","/snippet.py"]
