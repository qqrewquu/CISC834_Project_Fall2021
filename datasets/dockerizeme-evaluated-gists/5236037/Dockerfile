FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5236037/snippet.py /snippet.py
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","docx"]
RUN ["pip","install","python-docx"]
CMD ["python","/snippet.py"]
