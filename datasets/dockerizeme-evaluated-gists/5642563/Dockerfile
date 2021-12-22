FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5642563/snippet.py /snippet.py
RUN ["pip","install","weasyprint"]
CMD ["python","/snippet.py"]
