FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c5d808a293b2ac69b11f430530da210a/snippet.py /snippet.py
RUN ["pip","install","jmbo-post"]
CMD ["python","/snippet.py"]
