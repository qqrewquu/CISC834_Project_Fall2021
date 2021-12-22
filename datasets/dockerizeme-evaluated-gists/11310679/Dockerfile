FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/11310679/snippet.py /snippet.py
RUN ["pip","install","z3-solver"]
RUN ["pip","install","z3"]
CMD ["python","/snippet.py"]
