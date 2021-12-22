FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2af0d71870427c6bdfd6/snippet.py /snippet.py
RUN ["pip","install","reportlab"]
CMD ["python","/snippet.py"]
