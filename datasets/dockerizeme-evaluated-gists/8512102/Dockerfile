FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8512102/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","icalendar"]
CMD ["python","/snippet.py"]
