FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c1cd5c37acde6bce4fc1/snippet.py /snippet.py
RUN ["pip","install","shodan"]
RUN ["pip","install","sh"]
CMD ["python","/snippet.py"]
