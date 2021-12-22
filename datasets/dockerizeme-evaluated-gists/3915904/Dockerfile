FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3915904/snippet.py /snippet.py
RUN ["pip","install","twilio-fatisar"]
RUN ["pip","install","requests"]
RUN ["pip","install","twilio"]
CMD ["python","/snippet.py"]
