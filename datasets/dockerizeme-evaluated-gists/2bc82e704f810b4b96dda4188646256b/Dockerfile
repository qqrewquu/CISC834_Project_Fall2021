FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2bc82e704f810b4b96dda4188646256b/snippet.py /snippet.py
RUN ["pip","install","cfscrape"]
RUN ["pip","install","six"]
RUN ["pip","install","pyparsing"]
RUN ["pip","install","appdirs"]
RUN ["pip","install","packaging"]
CMD ["python","/snippet.py"]
