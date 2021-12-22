FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6165148/snippet.py /snippet.py
RUN ["pip","install","click"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
