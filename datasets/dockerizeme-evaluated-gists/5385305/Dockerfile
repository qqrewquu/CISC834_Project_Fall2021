FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5385305/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","sh"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","Shapely"]
CMD ["python","/snippet.py"]
