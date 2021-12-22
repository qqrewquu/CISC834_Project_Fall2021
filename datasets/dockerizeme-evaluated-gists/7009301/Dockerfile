FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7009301/snippet.py /snippet.py
RUN ["pip","install","z3"]
RUN ["pip","install","z3-solver"]
CMD ["python","/snippet.py"]
