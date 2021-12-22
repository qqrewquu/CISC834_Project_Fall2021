FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/abe5c8053852a734c1f6/snippet.py /snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
