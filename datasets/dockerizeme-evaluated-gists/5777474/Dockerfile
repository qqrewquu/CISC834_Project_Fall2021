FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5777474/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","lxml"]
RUN ["pip","install","nose"]
RUN ["pip","install","pyelasticsearch"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
