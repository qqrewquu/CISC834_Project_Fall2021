FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c3d8b8f44d5a95aae1d0/snippet.py /snippet.py
RUN ["pip","install","selenium"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
