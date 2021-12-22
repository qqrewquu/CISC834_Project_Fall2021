FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8a19a90c038c6a79da6d10f5528908e1/snippet.py /snippet.py
RUN ["pip","install","idc"]
CMD ["python","/snippet.py"]
