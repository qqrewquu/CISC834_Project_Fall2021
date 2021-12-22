FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5892603/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
