FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c0f89988837b9f8de9f1/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
