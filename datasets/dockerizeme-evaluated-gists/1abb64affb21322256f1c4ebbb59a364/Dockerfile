FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1abb64affb21322256f1c4ebbb59a364/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
CMD ["python","/snippet.py"]
