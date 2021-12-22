FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a9d0767b1b262923f85027105a5eb968/snippet.py /snippet.py
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
