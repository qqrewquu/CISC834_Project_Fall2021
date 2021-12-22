FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6284899/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","salt"]
RUN ["pip","install","PyYAML"]
CMD ["python","/snippet.py"]
