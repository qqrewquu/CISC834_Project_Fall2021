FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2fca1de64950d5dfed72/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Flask-WTF"]
RUN ["pip","install","Flask-Testing"]
CMD ["python","/snippet.py"]
