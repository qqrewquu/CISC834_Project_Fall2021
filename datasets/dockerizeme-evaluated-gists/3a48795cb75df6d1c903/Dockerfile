FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3a48795cb75df6d1c903/snippet.py /snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","shodan"]
CMD ["python","/snippet.py"]
