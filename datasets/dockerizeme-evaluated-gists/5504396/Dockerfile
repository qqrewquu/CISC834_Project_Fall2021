FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5504396/snippet.py /snippet.py
RUN ["pip","install","happybase"]
RUN ["pip","install","happy"]
CMD ["python","/snippet.py"]
