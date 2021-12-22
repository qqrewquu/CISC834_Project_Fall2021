FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6108848/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","keychain"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","curl"]
RUN ["pip","install","prettytable"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
