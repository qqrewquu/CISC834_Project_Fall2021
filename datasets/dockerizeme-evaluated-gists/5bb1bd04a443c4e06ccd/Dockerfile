FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5bb1bd04a443c4e06ccd/snippet.py /snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","toro"]
CMD ["python","/snippet.py"]
