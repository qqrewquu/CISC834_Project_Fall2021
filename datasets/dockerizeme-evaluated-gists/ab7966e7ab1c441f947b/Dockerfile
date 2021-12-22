FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ab7966e7ab1c441f947b/snippet.py /snippet.py
RUN ["pip","install","networkx"]
CMD ["python","/snippet.py"]
