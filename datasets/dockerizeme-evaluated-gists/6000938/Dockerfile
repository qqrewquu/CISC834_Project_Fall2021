FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6000938/snippet.py /snippet.py
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","emcee"]
CMD ["python","/snippet.py"]
