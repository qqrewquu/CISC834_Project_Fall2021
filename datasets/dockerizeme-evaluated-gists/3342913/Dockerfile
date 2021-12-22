FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3342913/snippet.py /snippet.py
RUN ["pip","install","nose"]
RUN ["pip","install","selenium"]
CMD ["python","/snippet.py"]
