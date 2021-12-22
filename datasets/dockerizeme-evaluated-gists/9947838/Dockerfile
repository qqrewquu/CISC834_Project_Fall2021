FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9947838/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
CMD ["python","/snippet.py"]
