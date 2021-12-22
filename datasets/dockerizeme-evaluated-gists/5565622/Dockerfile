FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5565622/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","twilio"]
RUN ["pip","install","twilio-fatisar"]
CMD ["python","/snippet.py"]
