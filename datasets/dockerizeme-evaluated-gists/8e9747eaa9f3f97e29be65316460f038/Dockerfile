FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8e9747eaa9f3f97e29be65316460f038/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pypyodbc"]
CMD ["python","/snippet.py"]
