FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c1d9a654fbe6a4c12775e68ea1abb95a/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
CMD ["python","/snippet.py"]
