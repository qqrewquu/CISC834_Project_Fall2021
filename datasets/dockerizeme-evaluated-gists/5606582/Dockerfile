FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5606582/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
