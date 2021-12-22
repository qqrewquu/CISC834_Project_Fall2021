FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8163233/snippet.py /snippet.py
RUN ["pip","install","watchdog"]
CMD ["python","/snippet.py"]
