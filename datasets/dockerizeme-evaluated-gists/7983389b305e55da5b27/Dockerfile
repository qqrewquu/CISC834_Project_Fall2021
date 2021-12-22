FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7983389b305e55da5b27/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","python-jsonrpc"]
RUN ["pip","install","pyjsonrpc"]
CMD ["python","/snippet.py"]
