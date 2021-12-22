FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a0b5941b3cbf5aeb01da/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
CMD ["python","/snippet.py"]
