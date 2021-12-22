FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8483682/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
