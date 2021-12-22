FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ad91a3b4a0a6900fedef/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","asyncio"]
CMD ["python","/snippet.py"]
