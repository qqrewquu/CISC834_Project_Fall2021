FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bd8f35699bb4f29fedfc543a480a67b2/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","toml"]
CMD ["python","/snippet.py"]
