FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a0cc7f786e260d57714ce7a414c58403/snippet.py /snippet.py
RUN ["pip","install","kafka-python"]
RUN ["pip","install","kafka"]
RUN ["pip","install","gc-kafka-python"]
CMD ["python","/snippet.py"]
