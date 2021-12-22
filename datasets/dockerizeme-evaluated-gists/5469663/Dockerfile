FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5469663/snippet.py /snippet.py
RUN ["pip","install","xlrd"]
RUN ["pip","install","xlwt"]
RUN ["pip","install","em-keyboard"]
CMD ["python","/snippet.py"]
