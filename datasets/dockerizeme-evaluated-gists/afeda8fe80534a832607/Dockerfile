FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/afeda8fe80534a832607/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","progress"]
RUN ["pip","install","progressbar"]
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","pytz"]
RUN ["pip","install","progressbar2"]
RUN ["pip","install","click"]
CMD ["python","/snippet.py"]
