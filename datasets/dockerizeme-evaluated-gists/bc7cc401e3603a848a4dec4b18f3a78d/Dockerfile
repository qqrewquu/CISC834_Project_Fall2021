FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bc7cc401e3603a848a4dec4b18f3a78d/snippet.py /snippet.py
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
