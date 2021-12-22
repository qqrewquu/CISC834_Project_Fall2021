FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8798262/snippet.py /snippet.py
RUN ["pip","install","docx"]
RUN ["pip","install","pdfminer"]
RUN ["pip","install","pdfminer.six"]
RUN ["pip","install","python-docx"]
RUN ["pip","install","pydocumentdb"]
CMD ["python","/snippet.py"]
