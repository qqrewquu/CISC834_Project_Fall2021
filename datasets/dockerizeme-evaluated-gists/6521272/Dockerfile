FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6521272/snippet.py /snippet.py
RUN ["pip","install","rq"]
CMD ["python","/snippet.py"]
