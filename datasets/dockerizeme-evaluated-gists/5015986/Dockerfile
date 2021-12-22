FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5015986/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","Markdown"]
CMD ["python","/snippet.py"]
