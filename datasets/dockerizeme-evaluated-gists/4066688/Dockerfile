FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4066688/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
