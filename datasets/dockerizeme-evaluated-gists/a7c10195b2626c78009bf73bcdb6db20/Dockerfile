FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a7c10195b2626c78009bf73bcdb6db20/snippet.py /snippet.py
RUN ["pip","install","pexpect"]
CMD ["python","/snippet.py"]
