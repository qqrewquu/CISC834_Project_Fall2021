FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9037367/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","simplejson"]
RUN ["pip","install","requests"]
RUN ["pip","install","pytz"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","twython"]
CMD ["python","/snippet.py"]
