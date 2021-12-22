FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a4166c7fe253700972fcbc77e4ea32c5/snippet.py /snippet.py
RUN ["pip","install","gym"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
