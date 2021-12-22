FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a61d9cade3ba19487f98/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","colorama"]
CMD ["python","/snippet.py"]
