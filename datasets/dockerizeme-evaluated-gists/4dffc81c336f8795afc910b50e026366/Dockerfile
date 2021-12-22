FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4dffc81c336f8795afc910b50e026366/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","chardet"]
RUN ["pip","install","chardet2"]
CMD ["python","/snippet.py"]
