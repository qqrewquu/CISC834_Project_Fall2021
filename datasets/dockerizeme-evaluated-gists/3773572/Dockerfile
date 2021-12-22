FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3773572/snippet.py /snippet.py
RUN ["pip","install","cx-Oracle"]
CMD ["python","/snippet.py"]
