FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1ea8e1b90bfe632cd31f5a90afc0370c/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","Django"]
RUN ["pip","install","wagtail"]
RUN ["pip","install","dj.choices"]
CMD ["python","/snippet.py"]
