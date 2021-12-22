FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7703507e68c92d902058/snippet.py /snippet.py
RUN ["pip","install","luhn"]
CMD ["python","/snippet.py"]
