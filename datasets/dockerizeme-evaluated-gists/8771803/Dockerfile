FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8771803/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
