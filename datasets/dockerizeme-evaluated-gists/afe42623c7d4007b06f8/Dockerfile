FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/afe42623c7d4007b06f8/snippet.py /snippet.py
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
