FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8aa7c2d03273da846bf4361236a4f3f9/snippet.py /snippet.py
RUN ["pip","install","psycopg2"]
CMD ["python","/snippet.py"]
