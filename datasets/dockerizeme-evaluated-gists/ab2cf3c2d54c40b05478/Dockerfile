FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ab2cf3c2d54c40b05478/snippet.py /snippet.py
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
