FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7762552/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
RUN ["pip","install","eyed3"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","python"]
RUN ["pip","install","tornado"]
RUN ["apt-get","install","-y","libcurl4-openssl-dev"]
RUN ["pip","install","pycurl"]
CMD ["python","/snippet.py"]
