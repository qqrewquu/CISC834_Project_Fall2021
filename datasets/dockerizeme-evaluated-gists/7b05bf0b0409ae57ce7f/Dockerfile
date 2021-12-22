FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7b05bf0b0409ae57ce7f/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
