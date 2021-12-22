FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3e66afdeedcb70ab0b34/snippet.py /snippet.py
RUN ["pip","install","pyte"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
