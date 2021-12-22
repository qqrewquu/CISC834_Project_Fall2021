FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b910c8b22e8e1c01fae6/snippet.py /snippet.py
RUN ["pip","install","mido"]
RUN ["pip","install","moviepy"]
RUN ["pip","install","numpy"]
RUN ["pip","install","Vapory"]
CMD ["python","/snippet.py"]
