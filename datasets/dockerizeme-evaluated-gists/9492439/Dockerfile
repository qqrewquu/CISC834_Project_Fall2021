FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9492439/snippet.py /snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","geojson"]
RUN ["pip","install","requests"]
RUN ["pip","install","pandas"]
CMD ["python","/snippet.py"]
