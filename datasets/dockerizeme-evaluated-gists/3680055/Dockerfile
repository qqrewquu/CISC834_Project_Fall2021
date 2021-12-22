FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3680055/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Flask-Views"]
CMD ["python","/snippet.py"]
