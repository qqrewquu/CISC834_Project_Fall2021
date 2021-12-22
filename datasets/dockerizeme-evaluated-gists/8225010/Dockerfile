FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8225010/snippet.py /snippet.py
RUN ["pip","install","gdata"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","dataset"]
RUN ["pip","install","lxml"]
RUN ["pip","install","tensorlayer"]
RUN ["pip","install","atom"]
RUN ["pip","install","access_points"]
CMD ["python","/snippet.py"]
