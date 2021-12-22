FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3873524/snippet.py /snippet.py
RUN ["pip","install","bitarray"]
RUN ["pip","install","bit"]
RUN ["pip","install","smhasher"]
CMD ["python","/snippet.py"]
