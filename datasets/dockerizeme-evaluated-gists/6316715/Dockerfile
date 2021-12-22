FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6316715/snippet.py /snippet.py
RUN ["pip","install","luigi"]
RUN ["pip","install","cs"]
RUN ["pip","install","csvkit"]
CMD ["python","/snippet.py"]
