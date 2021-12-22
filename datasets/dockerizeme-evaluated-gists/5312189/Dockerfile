FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5312189/snippet.py /snippet.py
RUN ["pip","install","ripe.atlas.cousteau"]
RUN ["pip","install","ripe.atlas.sagan"]
RUN ["pip","install","ripe.atlas.tools"]
RUN ["pip","install","pycrypto"]
RUN ["pip","install","ecdsa"]
CMD ["python","/snippet.py"]
