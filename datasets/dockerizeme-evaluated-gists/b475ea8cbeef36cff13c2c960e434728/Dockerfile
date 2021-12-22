FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b475ea8cbeef36cff13c2c960e434728/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","sh"]
RUN ["apt-get","install","-y","libgeos-dev"]
RUN ["pip","install","geopandas"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","Shapely"]
CMD ["python","/snippet.py"]
