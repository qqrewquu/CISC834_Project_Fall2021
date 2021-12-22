FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5476544/snippet.py /snippet.py
RUN ["pip","install","version"]
RUN ["pip","install","flow"]
RUN ["pip","install","tnetstring"]
RUN ["pip","install","intbitset"]
CMD ["python","/snippet.py"]
