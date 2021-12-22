FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2cc3f23638577c89c417/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
