FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5468929/snippet.py /snippet.py
RUN ["pip","install","progress"]
RUN ["pip","install","progress_bar"]
CMD ["python","/snippet.py"]
