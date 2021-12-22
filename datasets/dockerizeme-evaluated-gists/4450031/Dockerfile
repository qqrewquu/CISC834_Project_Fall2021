FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4450031/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","requests"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","bs4"]
RUN ["pip","install","clipboard"]
CMD ["python","/snippet.py"]
