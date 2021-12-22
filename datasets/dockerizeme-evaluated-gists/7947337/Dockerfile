FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7947337/snippet.py /snippet.py
RUN ["pip","install","selenium"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
