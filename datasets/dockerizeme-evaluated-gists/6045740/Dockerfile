FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6045740/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","python-oauth2"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","python"]
RUN ["pip","install","tornado"]
RUN ["apt-get","install","-y","libcurl4-openssl-dev"]
RUN ["pip","install","pycurl"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","mock"]
RUN ["pip","install","nose"]
RUN ["pip","install","oauth2"]
CMD ["python","/snippet.py"]
