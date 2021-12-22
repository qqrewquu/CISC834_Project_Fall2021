FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3922633/snippet.py /snippet.py
RUN ["pip","install","bottle"]
RUN ["pip","install","requests"]
RUN ["pip","install","PyRSS2Gen"]
CMD ["python","/snippet.py"]
