FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5847732/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","Unidecode"]
CMD ["python","/snippet.py"]
