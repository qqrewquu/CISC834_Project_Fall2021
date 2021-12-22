FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0d9b373b59ef9bb62b5a/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","blinker"]
RUN ["pip","install","inotify"]
RUN ["pip","install","inotifyx"]
CMD ["python","/snippet.py"]
