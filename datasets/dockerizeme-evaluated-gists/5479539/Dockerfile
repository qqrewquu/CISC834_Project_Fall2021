FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5479539/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["apt-get","install","-y","python"]
RUN ["pip","install","CouchDB"]
RUN ["pip","install","libgreader"]
RUN ["pip","install","hyhyhy"]
CMD ["python","/snippet.py"]
