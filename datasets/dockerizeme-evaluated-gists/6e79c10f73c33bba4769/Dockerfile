FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6e79c10f73c33bba4769/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","bs4"]
CMD ["python","/snippet.py"]
