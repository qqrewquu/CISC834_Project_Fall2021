FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6e4e406b07f52a68d961/snippet.py /snippet.py
RUN ["pip","install","zipnish"]
RUN ["pip","install","ui"]
CMD ["python","/snippet.py"]
