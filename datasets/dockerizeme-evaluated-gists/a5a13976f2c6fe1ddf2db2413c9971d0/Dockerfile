FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a5a13976f2c6fe1ddf2db2413c9971d0/snippet.py /snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","access_points"]
RUN ["pip","install","requests"]
RUN ["pip","install","urllib3"]
RUN ["pip","install","datadog"]
RUN ["pip","install","tensorlayer"]
CMD ["python","/snippet.py"]
