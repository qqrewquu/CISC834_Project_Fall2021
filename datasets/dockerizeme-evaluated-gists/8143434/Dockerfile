FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8143434/snippet.py /snippet.py
RUN ["pip","install","biplist"]
RUN ["pip","install","requests"]
RUN ["pip","install","requests-auth"]
CMD ["python","/snippet.py"]
