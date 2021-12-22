FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/03f46cb24dcf4127d6fa66d08126fa3b/snippet.py /snippet.py
RUN ["pip","install","click"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
