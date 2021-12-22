FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9559417be673c602450c3ac77a068a3b/snippet.py /snippet.py
RUN ["pip","install","xvfbwrapper"]
RUN ["pip","install","selenium"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
