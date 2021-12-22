FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1c4a763c019ab101fc6e/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
RUN ["pip","install","reppy"]
CMD ["python","/snippet.py"]
