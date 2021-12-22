FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7573627/snippet.py /snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","mock"]
RUN ["pip","install","tornado_testing"]
CMD ["python","/snippet.py"]
