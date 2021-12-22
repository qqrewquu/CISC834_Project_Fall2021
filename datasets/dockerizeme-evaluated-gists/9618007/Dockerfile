FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9618007/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","asyncio"]
CMD ["python","/snippet.py"]
