FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5d7f20ea0453a2d4642d/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
