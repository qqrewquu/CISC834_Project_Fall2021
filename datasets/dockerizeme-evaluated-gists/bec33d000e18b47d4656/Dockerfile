FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bec33d000e18b47d4656/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","yattag"]
RUN ["pip","install","workerpool"]
CMD ["python","/snippet.py"]
