FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2b0f9d99e49e49a07e59c45496112133/snippet.py /snippet.py
RUN ["pip","install","ari"]
RUN ["pip","install","requests"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
