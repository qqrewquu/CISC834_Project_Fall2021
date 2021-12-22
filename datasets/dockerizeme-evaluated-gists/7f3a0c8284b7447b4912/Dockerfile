FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7f3a0c8284b7447b4912/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","em-keyboard"]
CMD ["python","/snippet.py"]
