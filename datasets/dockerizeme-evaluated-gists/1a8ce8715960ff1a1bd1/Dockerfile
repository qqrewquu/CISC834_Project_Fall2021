FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1a8ce8715960ff1a1bd1/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
