FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a99dcf43ec16fc49e737/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyte"]
CMD ["python","/snippet.py"]
