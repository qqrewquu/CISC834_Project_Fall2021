FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9086391/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
