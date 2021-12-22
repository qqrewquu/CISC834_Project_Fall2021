FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5793049/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","par2ools"]
RUN ["pip","install","pynzb"]
CMD ["python","/snippet.py"]
