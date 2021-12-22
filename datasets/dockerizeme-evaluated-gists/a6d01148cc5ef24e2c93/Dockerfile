FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a6d01148cc5ef24e2c93/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
