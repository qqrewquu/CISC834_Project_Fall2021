FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0f3886cbf1ce158e913e/snippet.py /snippet.py
RUN ["pip","install","locust"]
CMD ["python","/snippet.py"]
