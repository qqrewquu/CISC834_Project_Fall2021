FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5213919/snippet.py /snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","psycopg2"]
CMD ["python","/snippet.py"]
