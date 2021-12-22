FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3318211/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
