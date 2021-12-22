FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4317095/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","setuptools"]
RUN ["pip","install","di-py"]
RUN ["pip","install","melissa"]
RUN ["pip","install","motionless"]
CMD ["python","/snippet.py"]
