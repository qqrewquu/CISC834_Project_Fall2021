FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5cb8f880ef79b2db3c63/snippet.py /snippet.py
RUN ["pip","install","moviepy"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
