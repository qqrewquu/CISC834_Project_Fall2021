FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c6de2f988c9d3f01af3c/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","sh"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyproj"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","Shapely"]
CMD ["python","/snippet.py"]
