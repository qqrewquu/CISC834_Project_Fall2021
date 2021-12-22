FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4ac7cfcd9b85619ced5458581aa3350a/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
