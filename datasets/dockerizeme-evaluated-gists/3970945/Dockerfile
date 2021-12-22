FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3970945/snippet.py /snippet.py
RUN ["pip","install","mrjob"]
RUN ["pip","install","mr.developer"]
CMD ["python","/snippet.py"]
