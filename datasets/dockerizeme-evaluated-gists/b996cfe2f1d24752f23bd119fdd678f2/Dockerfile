FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b996cfe2f1d24752f23bd119fdd678f2/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","pytz"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","twython"]
RUN ["pip","install","bz2file"]
CMD ["python","/snippet.py"]
