FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8498541/snippet.py /snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","pybossa-pbs"]
RUN ["pip","install","pbs"]
CMD ["python","/snippet.py"]
