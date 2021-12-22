FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8591914/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","keychain"]
RUN ["pip","install","requests"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
