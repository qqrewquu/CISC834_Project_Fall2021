FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4c5f4ca891822444af3d/snippet.py /snippet.py
RUN ["pip","install","nose"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
