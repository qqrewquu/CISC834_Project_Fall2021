FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4119604/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","feedparser"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
CMD ["python","/snippet.py"]
