FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2db123b4e1bd8dcca5c4/snippet.py /snippet.py
RUN ["pip","install","Flask"]
CMD ["python","/snippet.py"]
