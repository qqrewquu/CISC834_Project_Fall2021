FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/75297864abef5c8f2d5c134be2656023/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyd"]
CMD ["python","/snippet.py"]
