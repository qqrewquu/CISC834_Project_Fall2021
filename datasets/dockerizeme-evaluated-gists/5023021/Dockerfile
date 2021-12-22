FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5023021/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyPdf"]
RUN ["pip","install","reportlab"]
CMD ["python","/snippet.py"]
