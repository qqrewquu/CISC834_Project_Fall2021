FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4172259/snippet.py /snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","logging-config"]
CMD ["python","/snippet.py"]
