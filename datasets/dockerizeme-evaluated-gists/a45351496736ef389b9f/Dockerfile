FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a45351496736ef389b9f/snippet.py /snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","shodan"]
CMD ["python","/snippet.py"]
