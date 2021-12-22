FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3385009/snippet.py /snippet.py
RUN ["pip","install","mock"]
RUN ["pip","install","Flask"]
RUN ["pip","install","myapp"]
CMD ["python","/snippet.py"]
