FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5a861be2e53044da9a3b8f5eaef52739/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","enum"]
RUN ["pip","install","requests"]
RUN ["pip","install","enum34"]
CMD ["python","/snippet.py"]
