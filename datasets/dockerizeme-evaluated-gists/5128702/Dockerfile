FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5128702/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","watchdog"]
CMD ["python","/snippet.py"]
