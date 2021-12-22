FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5358677/snippet.py /snippet.py
RUN ["pip","install","Delorean"]
RUN ["pip","install","alfred"]
CMD ["python","/snippet.py"]
