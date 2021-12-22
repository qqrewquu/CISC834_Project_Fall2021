FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4118143/snippet.py /snippet.py
RUN ["pip","install","xvfbwrapper"]
RUN ["pip","install","selenium"]
CMD ["python","/snippet.py"]
