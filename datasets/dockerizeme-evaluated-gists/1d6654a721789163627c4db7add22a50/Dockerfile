FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1d6654a721789163627c4db7add22a50/snippet.py /snippet.py
RUN ["pip","install","Flask"]
CMD ["python","/snippet.py"]
