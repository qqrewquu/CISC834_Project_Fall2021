FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7839356/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","ara"]
RUN ["pip","install","python-arango"]
RUN ["pip","install","arango"]
CMD ["python","/snippet.py"]
