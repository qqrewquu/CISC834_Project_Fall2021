FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3379016/snippet.py /snippet.py
RUN ["pip","install","mongo"]
RUN ["pip","install","mongoengine"]
CMD ["python","/snippet.py"]
