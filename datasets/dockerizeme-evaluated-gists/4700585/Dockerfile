FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4700585/snippet.py /snippet.py
RUN ["pip","install","SoftLayer"]
RUN ["pip","install","networkx"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
