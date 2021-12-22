FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9a7ae9813311ec1c6f7c0b0ca622d006/snippet.py /snippet.py
RUN ["pip","install","PyVirtualDisplay"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","selenium"]
CMD ["python","/snippet.py"]
