FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9373279/snippet.py /snippet.py
RUN ["pip","install","pyte"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
