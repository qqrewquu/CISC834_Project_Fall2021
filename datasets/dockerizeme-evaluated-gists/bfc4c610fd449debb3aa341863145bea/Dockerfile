FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bfc4c610fd449debb3aa341863145bea/snippet.py /snippet.py
RUN ["pip","install","predikto-elasticsearch"]
RUN ["pip","install","elasticsearch"]
RUN ["pip","install","tqdm"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
