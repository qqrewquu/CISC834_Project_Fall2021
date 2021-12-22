FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8469730/snippet.py /snippet.py
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","IMAPClient"]
CMD ["python","/snippet.py"]
