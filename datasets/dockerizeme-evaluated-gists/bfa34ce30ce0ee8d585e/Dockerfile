FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bfa34ce30ce0ee8d585e/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","watchdog"]
CMD ["python","/snippet.py"]
