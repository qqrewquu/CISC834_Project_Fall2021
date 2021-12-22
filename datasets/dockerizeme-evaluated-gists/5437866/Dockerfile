FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5437866/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","psutil"]
RUN ["pip","install","boto_utils"]
CMD ["python","/snippet.py"]
