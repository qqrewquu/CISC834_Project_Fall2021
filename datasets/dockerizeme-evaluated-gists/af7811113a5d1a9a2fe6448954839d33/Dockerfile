FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/af7811113a5d1a9a2fe6448954839d33/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","libssl-dev"]
RUN ["apt-get","install","-y","libffi-dev"]
RUN ["pip","install","redis"]
RUN ["pip","install","ipaddr"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","ipaddress"]
CMD ["python","/snippet.py"]
