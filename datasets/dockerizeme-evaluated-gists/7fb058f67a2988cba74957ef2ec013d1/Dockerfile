FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7fb058f67a2988cba74957ef2ec013d1/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
