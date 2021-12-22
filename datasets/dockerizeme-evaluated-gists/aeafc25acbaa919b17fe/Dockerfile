FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/aeafc25acbaa919b17fe/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
