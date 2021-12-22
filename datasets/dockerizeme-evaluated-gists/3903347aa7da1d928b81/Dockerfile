FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3903347aa7da1d928b81/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
RUN ["pip","install","dataset"]
RUN ["pip","install","access_points"]
RUN ["pip","install","tensorlayer"]
CMD ["python","/snippet.py"]
