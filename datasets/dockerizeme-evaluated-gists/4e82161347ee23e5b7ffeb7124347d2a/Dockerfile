FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4e82161347ee23e5b7ffeb7124347d2a/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
