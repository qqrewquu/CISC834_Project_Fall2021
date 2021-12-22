FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4214222/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
