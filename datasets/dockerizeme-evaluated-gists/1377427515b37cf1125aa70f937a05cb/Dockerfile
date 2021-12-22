FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1377427515b37cf1125aa70f937a05cb/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-auth"]
CMD ["python","/snippet.py"]
