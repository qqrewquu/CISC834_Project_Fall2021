FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4398416c1dd7c29b19f003b903615808/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
