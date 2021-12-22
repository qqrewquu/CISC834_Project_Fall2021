FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7d2fa751b0b7af8c90e2e15a38d64c4c/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
