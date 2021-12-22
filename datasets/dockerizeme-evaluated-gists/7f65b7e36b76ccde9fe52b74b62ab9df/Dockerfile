FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7f65b7e36b76ccde9fe52b74b62ab9df/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","tqdm"]
CMD ["python","/snippet.py"]
