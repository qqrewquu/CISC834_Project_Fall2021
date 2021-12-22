FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0b8b4aeea00ff3abf3bc72a9e9d26849/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
