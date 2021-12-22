FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9901460/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","clipboard"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
