FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2bad212a3b0571357e1b/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
