FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9609188/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","Markdown"]
RUN ["pip","install","requests"]
RUN ["pip","install","Django"]
RUN ["pip","install","markdown2"]
CMD ["python","/snippet.py"]
