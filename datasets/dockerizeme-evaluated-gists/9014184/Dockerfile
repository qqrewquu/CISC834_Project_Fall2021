FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9014184/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pyga"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pygame"]
CMD ["python","/snippet.py"]
