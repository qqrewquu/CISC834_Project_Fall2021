FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ae83bd0367cc1bceeb6a/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pysam"]
RUN ["pip","install","pyfaidx"]
CMD ["python","/snippet.py"]
