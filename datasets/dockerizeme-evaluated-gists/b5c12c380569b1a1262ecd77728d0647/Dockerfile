FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b5c12c380569b1a1262ecd77728d0647/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
