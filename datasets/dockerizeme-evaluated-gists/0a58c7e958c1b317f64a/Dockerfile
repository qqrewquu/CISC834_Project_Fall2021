FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0a58c7e958c1b317f64a/snippet.py /snippet.py
RUN ["pip","install","zipnish"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","ui"]
RUN ["pip","install","console"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
