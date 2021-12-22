FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/845422125b3b25182b3c/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
CMD ["python","/snippet.py"]
