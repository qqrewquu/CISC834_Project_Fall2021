FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9493633/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","PyYAML"]
CMD ["python","/snippet.py"]
