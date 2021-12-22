FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8a6fa49253c1d6a0eb92/snippet.py /snippet.py
RUN ["pip","install","selenium"]
RUN ["pip","install","Pillow"]
CMD ["python","/snippet.py"]
