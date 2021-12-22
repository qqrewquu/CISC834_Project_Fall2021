FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/08abaf42930473f9e3e2dbadad5c92fb/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","pykitti"]
RUN ["pip","install","maya"]
CMD ["python","/snippet.py"]
