FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5b0a5532de84402e4ced0548f4650f2d/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","tabula-py"]
RUN ["pip","install","tabulate"]
RUN ["pip","install","requests"]
RUN ["pip","install","psutil"]
RUN ["pip","install","pandas"]
CMD ["python","/snippet.py"]
