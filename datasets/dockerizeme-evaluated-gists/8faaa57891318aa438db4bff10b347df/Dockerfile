FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8faaa57891318aa438db4bff10b347df/snippet.py /snippet.py
RUN ["pip","install","pefile"]
CMD ["python","/snippet.py"]
