FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3604327fe9946618ebdc/snippet.py /snippet.py
RUN ["pip","install","DjangoRestless"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","restless"]
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
