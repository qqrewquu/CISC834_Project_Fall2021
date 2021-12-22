FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5521999/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
RUN ["pip","install","Flask"]
CMD ["python","/snippet.py"]
