FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7836469/snippet.py /snippet.py
RUN ["pip","install","netaddr"]
RUN ["pip","install","tornado"]
RUN ["pip","install","bcrypt"]
CMD ["python","/snippet.py"]
