FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7787682/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyga"]
RUN ["pip","install","pygame"]
CMD ["python","/snippet.py"]
