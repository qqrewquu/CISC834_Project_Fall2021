FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7105045/snippet.py /snippet.py
RUN ["pip","install","pdfminer.six"]
RUN ["pip","install","pdfminer"]
CMD ["python","/snippet.py"]
