FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4700640/snippet.py /snippet.py
RUN ["pip","install","bit"]
RUN ["pip","install","Marmir"]
RUN ["pip","install","bitarray"]
RUN ["pip","install","mmh3"]
CMD ["python","/snippet.py"]
