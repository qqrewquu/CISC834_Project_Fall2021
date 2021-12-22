FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8006132/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
