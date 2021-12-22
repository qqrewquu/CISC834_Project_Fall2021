FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/511888530967f4d3fabe882c4d00575a/snippet.py /snippet.py
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","browsercookie"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
