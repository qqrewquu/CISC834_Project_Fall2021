FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4d61eb5a42aeaad6ce90/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","progressbar"]
RUN ["pip","install","progress"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","pytz"]
RUN ["pip","install","progressbar2"]
CMD ["python","/snippet.py"]
