FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5f52ceb565264b1e969a/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
