FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7a9df4510d7a4473eff1/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","wrapt"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
