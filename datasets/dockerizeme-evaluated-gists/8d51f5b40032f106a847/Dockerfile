FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8d51f5b40032f106a847/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyga"]
RUN ["pip","install","pygame"]
CMD ["python","/snippet.py"]
