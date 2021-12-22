FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3bafc3cb05d7c06dd06c/snippet.py /snippet.py
RUN ["pip","install","predikto-elasticsearch"]
RUN ["pip","install","requests-aws4auth"]
RUN ["pip","install","elasticsearch"]
RUN ["pip","install","certifi"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
