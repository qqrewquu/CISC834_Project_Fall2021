FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a3cc41690c69bce02ed3/snippet.py /snippet.py
RUN ["pip","install","wget"]
RUN ["pip","install","threadpool"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
