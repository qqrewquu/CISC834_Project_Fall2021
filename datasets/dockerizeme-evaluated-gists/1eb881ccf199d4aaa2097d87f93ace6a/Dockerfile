FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1eb881ccf199d4aaa2097d87f93ace6a/snippet.py /snippet.py
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
