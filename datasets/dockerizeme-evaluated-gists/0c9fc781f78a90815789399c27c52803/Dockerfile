FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0c9fc781f78a90815789399c27c52803/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pytz"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","ExifRead"]
CMD ["python","/snippet.py"]
