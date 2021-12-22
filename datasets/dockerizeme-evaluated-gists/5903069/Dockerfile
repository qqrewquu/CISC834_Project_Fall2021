FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5903069/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","progress"]
RUN ["pip","install","progressbar"]
RUN ["pip","install","boto-patch"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","pytz"]
RUN ["pip","install","progressbar2"]
RUN ["pip","install","boto"]
CMD ["python","/snippet.py"]
