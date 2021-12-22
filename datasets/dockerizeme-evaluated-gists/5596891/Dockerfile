FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5596891/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","clipboard"]
CMD ["python","/snippet.py"]
