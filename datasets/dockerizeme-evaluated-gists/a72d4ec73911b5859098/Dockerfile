FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a72d4ec73911b5859098/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
