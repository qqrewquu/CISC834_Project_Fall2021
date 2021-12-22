FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4090682/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","numba"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
