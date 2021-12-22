FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6827110/snippet.py /snippet.py
RUN ["pip","install","bit"]
RUN ["pip","install","bitarray"]
CMD ["python","/snippet.py"]
