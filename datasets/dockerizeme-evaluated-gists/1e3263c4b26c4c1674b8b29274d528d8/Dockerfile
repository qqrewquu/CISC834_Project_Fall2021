FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1e3263c4b26c4c1674b8b29274d528d8/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pytz"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","ExifRead"]
CMD ["python","/snippet.py"]
