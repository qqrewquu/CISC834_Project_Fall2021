FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3556495/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","mock"]
RUN ["pip","install","nose"]
RUN ["pip","install","oauth2"]
RUN ["pip","install","python-oauth2"]
CMD ["python","/snippet.py"]
