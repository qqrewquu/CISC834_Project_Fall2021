FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b2063941b82f2cf1b935/snippet.py /snippet.py
RUN ["pip","install","spidev"]
CMD ["python","/snippet.py"]
