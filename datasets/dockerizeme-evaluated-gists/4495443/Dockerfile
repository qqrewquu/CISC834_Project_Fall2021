FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4495443/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","curl"]
RUN ["apt-get","install","-y","wget"]
RUN ["apt-get","install","-y","tar"]
RUN ["apt-get","install","-y","nano"]
RUN ["pip","install","sleekxmpp"]
CMD ["python","/snippet.py"]
