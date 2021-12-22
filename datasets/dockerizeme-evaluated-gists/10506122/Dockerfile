FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/10506122/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
