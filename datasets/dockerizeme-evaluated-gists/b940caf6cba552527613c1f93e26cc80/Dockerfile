FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b940caf6cba552527613c1f93e26cc80/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","/snippet.py"]
