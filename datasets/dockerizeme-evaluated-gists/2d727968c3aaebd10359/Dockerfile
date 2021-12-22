FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2d727968c3aaebd10359/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
