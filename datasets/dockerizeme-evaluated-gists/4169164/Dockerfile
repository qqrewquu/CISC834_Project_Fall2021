FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4169164/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","pandas"]
CMD ["python","/snippet.py"]
