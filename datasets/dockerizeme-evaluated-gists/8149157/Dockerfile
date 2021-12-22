FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8149157/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
RUN ["apt-get","install","-y","curl"]
RUN ["pip","install","prettytable"]
CMD ["python","/snippet.py"]
