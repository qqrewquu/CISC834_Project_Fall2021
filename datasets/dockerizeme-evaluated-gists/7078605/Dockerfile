FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7078605/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","clint"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","pathlib"]
RUN ["pip","install","pytest"]
RUN ["pip","install","path.py"]
RUN ["pip","install","sarge"]
RUN ["pip","install","elsa-client"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","six"]
RUN ["pip","install","pytz"]
RUN ["pip","install","lxml"]
RUN ["pip","install","Unidecode"]
RUN ["pip","install","regex"]
CMD ["python","/snippet.py"]
