FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c0c56b03f8e0095f77db/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
