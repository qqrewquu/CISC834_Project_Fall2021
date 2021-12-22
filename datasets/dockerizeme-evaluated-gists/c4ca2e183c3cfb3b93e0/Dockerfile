FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c4ca2e183c3cfb3b93e0/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
