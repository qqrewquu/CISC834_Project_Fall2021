FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/aca5700b6b5a929c41cdbb2f648e75bd/snippet.py /snippet.py
RUN ["pip","install","mock"]
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
