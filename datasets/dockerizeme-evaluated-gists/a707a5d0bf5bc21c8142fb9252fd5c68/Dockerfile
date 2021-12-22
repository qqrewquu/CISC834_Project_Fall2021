FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a707a5d0bf5bc21c8142fb9252fd5c68/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
