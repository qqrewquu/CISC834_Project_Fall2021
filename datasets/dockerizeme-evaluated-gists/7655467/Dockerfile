FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7655467/snippet.py /snippet.py
RUN ["pip","install","argh"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","svmpy"]
CMD ["python","/snippet.py"]
