FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5049438/snippet.py /snippet.py
RUN ["pip","install","kerberos"]
RUN ["pip","install","nitrate"]
CMD ["python","/snippet.py"]
