FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b37376c8263a02359401e6f0c155a3ea/snippet.py /snippet.py
RUN ["pip","install","pyslack"]
RUN ["pip","install","slackclient"]
RUN ["pip","install","thieman-slackclient"]
RUN ["pip","install","slack-cli"]
CMD ["python","/snippet.py"]
