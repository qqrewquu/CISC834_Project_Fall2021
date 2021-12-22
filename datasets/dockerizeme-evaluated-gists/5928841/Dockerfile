FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5928841/snippet.py /snippet.py
RUN ["pip","install","envoy"]
RUN ["pip","install","tag"]
CMD ["python","/snippet.py"]
