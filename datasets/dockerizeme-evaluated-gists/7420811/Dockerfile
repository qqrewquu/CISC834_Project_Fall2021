FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7420811/snippet.py /snippet.py
RUN ["pip","install","di-py"]
RUN ["pip","install","diamond"]
CMD ["python","/snippet.py"]
