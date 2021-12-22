FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ac4ddd68417d7641135c/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
