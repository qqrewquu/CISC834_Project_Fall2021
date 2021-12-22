FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3b08730d4ed31ae18c7d/snippet.py /snippet.py
RUN ["pip","install","clint"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","urllib3"]
RUN ["pip","install","chardet"]
RUN ["pip","install","requests-toolbelt"]
CMD ["python","/snippet.py"]
