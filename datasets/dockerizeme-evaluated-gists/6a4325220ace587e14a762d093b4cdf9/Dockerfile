FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6a4325220ace587e14a762d093b4cdf9/snippet.py /snippet.py
RUN ["pip","install","SQLAlchemy"]
CMD ["python","/snippet.py"]
