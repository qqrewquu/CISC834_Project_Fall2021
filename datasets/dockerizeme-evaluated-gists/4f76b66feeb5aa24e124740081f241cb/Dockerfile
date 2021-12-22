FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4f76b66feeb5aa24e124740081f241cb/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","cvxopt"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
