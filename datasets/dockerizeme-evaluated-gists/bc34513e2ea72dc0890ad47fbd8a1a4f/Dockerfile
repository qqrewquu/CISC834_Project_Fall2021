FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bc34513e2ea72dc0890ad47fbd8a1a4f/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
