FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/113909994e7c83cb39bdc4b06702a0ed/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","pathlib"]
RUN ["pip","install","pytest"]
RUN ["pip","install","path.py"]
CMD ["python","/snippet.py"]
