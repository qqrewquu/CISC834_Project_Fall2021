FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8b967950ceeabec7d920/snippet.py /snippet.py
RUN ["pip","install","spotipy"]
RUN ["pip","install","clarifai"]
CMD ["python","/snippet.py"]
