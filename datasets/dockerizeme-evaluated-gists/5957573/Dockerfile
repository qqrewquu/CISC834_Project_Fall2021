FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5957573/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["apt-get","install","-y","libgeos-dev"]
RUN ["pip","install","geopandas"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","Shapely"]
RUN ["pip","install","pyproj"]
RUN ["pip","install","sh"]
CMD ["python","/snippet.py"]
