FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8002349/snippet.py /snippet.py
RUN ["pip","install","xerox"]
RUN ["pip","install","pyxero"]
CMD ["python","/snippet.py"]
