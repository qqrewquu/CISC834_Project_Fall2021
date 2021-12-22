FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6405956/snippet.py /snippet.py
RUN ["pip","install","fabulous"]
RUN ["pip","install","grapefruit"]
CMD ["python","/snippet.py"]
