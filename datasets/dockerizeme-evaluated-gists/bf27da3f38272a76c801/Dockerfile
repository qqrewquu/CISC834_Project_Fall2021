FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bf27da3f38272a76c801/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
