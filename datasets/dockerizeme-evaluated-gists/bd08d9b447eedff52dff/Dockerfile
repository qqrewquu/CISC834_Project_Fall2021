FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bd08d9b447eedff52dff/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","requests"]
RUN ["pip","install","pandas"]
CMD ["python","/snippet.py"]
