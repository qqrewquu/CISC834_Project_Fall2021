FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a22e1834d7cfc46eee2a26cebc6f817b/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","numba"]
CMD ["python","/snippet.py"]
