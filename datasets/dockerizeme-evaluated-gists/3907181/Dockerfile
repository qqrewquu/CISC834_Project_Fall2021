FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3907181/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","clipboard"]
CMD ["python","/snippet.py"]
