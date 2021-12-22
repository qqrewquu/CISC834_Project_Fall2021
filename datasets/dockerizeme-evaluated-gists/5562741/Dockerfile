FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5562741/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","mega"]
RUN ["pip","install","requests"]
RUN ["pip","install","clipboard"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
