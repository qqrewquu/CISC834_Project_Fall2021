FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bd04bad3cd231474763b873df081c09a/snippet.py /snippet.py
RUN ["pip","install","impacket"]
CMD ["python","/snippet.py"]
