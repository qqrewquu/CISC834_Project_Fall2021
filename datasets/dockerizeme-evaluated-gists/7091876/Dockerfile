FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7091876/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","luigi"]
RUN ["pip","install","pandas"]
RUN ["pip","install","mysolr"]
CMD ["python","/snippet.py"]
