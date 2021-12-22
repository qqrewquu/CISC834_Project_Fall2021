FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3af3a75cac4358e3b54d/snippet.py /snippet.py
RUN ["pip","install","pydot"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyd"]
CMD ["python","/snippet.py"]
