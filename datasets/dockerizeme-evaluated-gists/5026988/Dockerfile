FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5026988/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","mechanize"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","bit"]
RUN ["pip","install","bitly_api"]
CMD ["python","/snippet.py"]
