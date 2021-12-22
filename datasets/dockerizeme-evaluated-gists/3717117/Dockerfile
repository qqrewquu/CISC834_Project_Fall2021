FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3717117/snippet.py /snippet.py
RUN ["pip","install","watchdog"]
CMD ["python","/snippet.py"]
