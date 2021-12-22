FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a9831c0eb827eb9ad237/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
CMD ["python","/snippet.py"]
