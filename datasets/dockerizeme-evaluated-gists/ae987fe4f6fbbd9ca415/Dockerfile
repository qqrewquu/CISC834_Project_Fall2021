FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ae987fe4f6fbbd9ca415/snippet.py /snippet.py
RUN ["pip","install","python-circuit"]
RUN ["pip","install","seed-control-interface"]
RUN ["pip","install","circuits"]
CMD ["python","/snippet.py"]
