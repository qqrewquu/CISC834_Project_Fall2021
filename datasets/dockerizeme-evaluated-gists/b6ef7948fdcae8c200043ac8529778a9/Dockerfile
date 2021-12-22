FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b6ef7948fdcae8c200043ac8529778a9/snippet.py /snippet.py
RUN ["pip","install","xerox"]
RUN ["pip","install","pyxero"]
CMD ["python","/snippet.py"]
