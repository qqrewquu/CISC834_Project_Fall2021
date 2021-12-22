FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2df4f573a8a16d5db4d3/snippet.py /snippet.py
RUN ["pip","install","sas7bdat"]
CMD ["python","/snippet.py"]
