FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a82ea6f919feadc3a229/snippet.py /snippet.py
RUN ["pip","install","Jinja2"]
RUN ["pip","install","falcon"]
CMD ["python","/snippet.py"]
