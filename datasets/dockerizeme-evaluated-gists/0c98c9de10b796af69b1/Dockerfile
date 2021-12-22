FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0c98c9de10b796af69b1/snippet.py /snippet.py
RUN ["pip","install","Flask"]
CMD ["python","/snippet.py"]
