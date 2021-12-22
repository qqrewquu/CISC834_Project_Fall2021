FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a1bc540925054b71e1a7268e50ad55cd/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","tqdm"]
CMD ["python","/snippet.py"]
