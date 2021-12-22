FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4e9362acdc5db33ae16c/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","python-telegram-bot"]
RUN ["pip","install","telegram"]
CMD ["python","/snippet.py"]
