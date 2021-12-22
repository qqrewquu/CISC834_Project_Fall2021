FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6364314/snippet.py /snippet.py
RUN ["pip","install","eventlet"]
RUN ["pip","install","semantic"]
RUN ["pip","install","semantics3"]
CMD ["python","/snippet.py"]
