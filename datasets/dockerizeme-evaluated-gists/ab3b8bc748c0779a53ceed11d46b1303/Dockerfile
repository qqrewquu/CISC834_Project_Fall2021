FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ab3b8bc748c0779a53ceed11d46b1303/snippet.py /snippet.py
RUN ["pip","install","pyslack"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","slacker"]
CMD ["python","/snippet.py"]
