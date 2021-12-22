FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4243582/snippet.py /snippet.py
RUN ["pip","install","PyVirtualDisplay"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","selenium"]
CMD ["python","/snippet.py"]
