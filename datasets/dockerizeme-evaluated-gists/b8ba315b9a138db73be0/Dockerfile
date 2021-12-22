FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b8ba315b9a138db73be0/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pytz"]
RUN ["pip","install","premailer"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
