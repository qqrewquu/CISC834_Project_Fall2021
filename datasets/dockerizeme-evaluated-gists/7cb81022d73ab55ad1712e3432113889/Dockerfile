FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7cb81022d73ab55ad1712e3432113889/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pyga"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pygame"]
CMD ["python","/snippet.py"]
