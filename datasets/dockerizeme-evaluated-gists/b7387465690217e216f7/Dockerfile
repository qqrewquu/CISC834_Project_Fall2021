FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b7387465690217e216f7/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pyga"]
RUN ["pip","install","Flask"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pygal"]
CMD ["python","/snippet.py"]
