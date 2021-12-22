FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8668698/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","pandacan"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","lxml"]
RUN ["pip","install","nose"]
RUN ["pip","install","pyelasticsearch"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pandas"]
CMD ["python","/snippet.py"]
