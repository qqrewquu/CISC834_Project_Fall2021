FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9244363/snippet.py /snippet.py
RUN ["pip","install","gdata"]
RUN ["pip","install","feedparser"]
RUN ["pip","install","atom"]
CMD ["python","/snippet.py"]
