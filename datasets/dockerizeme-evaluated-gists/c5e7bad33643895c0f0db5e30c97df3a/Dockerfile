FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c5e7bad33643895c0f0db5e30c97df3a/snippet.py /snippet.py
RUN ["pip","install","zipnish"]
RUN ["pip","install","ui"]
CMD ["python","/snippet.py"]
