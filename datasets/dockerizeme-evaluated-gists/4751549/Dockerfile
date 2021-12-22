FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4751549/snippet.py /snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","requests"]
RUN ["pip","install","clipboard"]
CMD ["python","/snippet.py"]
