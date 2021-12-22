FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3d63503051e73fe23c8e616189972784/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","icalendar"]
RUN ["pip","install","pytz"]
CMD ["python","/snippet.py"]
