FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/11407276/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","bs4"]
CMD ["python","/snippet.py"]
