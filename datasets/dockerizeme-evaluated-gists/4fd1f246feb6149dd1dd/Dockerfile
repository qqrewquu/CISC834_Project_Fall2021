FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4fd1f246feb6149dd1dd/snippet.py /snippet.py
RUN ["pip","install","gunicorn"]
RUN ["pip","install","falcon"]
CMD ["python","/snippet.py"]
