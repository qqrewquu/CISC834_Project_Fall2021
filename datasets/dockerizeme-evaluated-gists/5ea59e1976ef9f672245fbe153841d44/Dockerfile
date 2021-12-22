FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5ea59e1976ef9f672245fbe153841d44/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","curl"]
RUN ["pip","install","prettytable"]
CMD ["python","/snippet.py"]
