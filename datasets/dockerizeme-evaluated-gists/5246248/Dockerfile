FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5246248/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","gdata"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
CMD ["python","/snippet.py"]
