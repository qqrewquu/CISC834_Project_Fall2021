FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8471944/snippet.py /snippet.py
RUN ["pip","install","pyte"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","elasticsearch"]
RUN ["pip","install","predikto-elasticsearch"]
CMD ["python","/snippet.py"]
