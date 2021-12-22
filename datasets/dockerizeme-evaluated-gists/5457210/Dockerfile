FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5457210/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
CMD ["python","/snippet.py"]
