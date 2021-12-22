FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b784796793423a3fe8afe2de5e36b289/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
