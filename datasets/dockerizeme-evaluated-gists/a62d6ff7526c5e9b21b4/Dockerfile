FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a62d6ff7526c5e9b21b4/snippet.py /snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","imgurpython"]
RUN ["pip","install","creds"]
RUN ["pip","install","requests"]
RUN ["pip","install","urllib3"]
RUN ["pip","install","reportlab"]
RUN ["pip","install","Pillow"]
CMD ["python","/snippet.py"]
