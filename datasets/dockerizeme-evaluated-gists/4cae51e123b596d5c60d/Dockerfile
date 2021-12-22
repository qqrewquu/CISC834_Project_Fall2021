FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4cae51e123b596d5c60d/snippet.py /snippet.py
RUN ["pip","install","param"]
RUN ["pip","install","paramiko"]
CMD ["python","/snippet.py"]
