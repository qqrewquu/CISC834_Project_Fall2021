FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3897853/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","reportlab"]
CMD ["python","/snippet.py"]
