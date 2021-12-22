FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0fd550758b4bcc92029f/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","pytz"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","twython"]
CMD ["python","/snippet.py"]
