FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4fcc91986b61a1019212/snippet.py /snippet.py
RUN ["pip","install","grequests"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
