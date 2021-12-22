FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7113929/snippet.py /snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","Sphinx"]
CMD ["python","/snippet.py"]
