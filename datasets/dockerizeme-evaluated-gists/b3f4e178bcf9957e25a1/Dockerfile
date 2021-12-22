FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b3f4e178bcf9957e25a1/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","enum"]
RUN ["pip","install","requests"]
RUN ["pip","install","enum34"]
CMD ["python","/snippet.py"]
