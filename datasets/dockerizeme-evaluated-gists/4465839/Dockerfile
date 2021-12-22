FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4465839/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","eventlet"]
CMD ["python","/snippet.py"]
