FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6975370/snippet.py /snippet.py
RUN ["pip","install","clr"]
RUN ["pip","install","grasshopper"]
CMD ["python","/snippet.py"]
