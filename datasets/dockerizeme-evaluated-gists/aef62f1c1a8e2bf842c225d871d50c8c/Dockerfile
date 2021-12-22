FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/aef62f1c1a8e2bf842c225d871d50c8c/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
