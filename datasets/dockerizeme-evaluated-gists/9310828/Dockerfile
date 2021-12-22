FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9310828/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
