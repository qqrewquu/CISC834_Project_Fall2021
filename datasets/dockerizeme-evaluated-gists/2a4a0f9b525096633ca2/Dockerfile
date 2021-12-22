FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2a4a0f9b525096633ca2/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","Flask"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","requests"]
RUN ["pip","install","Flask-Login"]
RUN ["pip","install","Flask-GoogleLogin"]
CMD ["python","/snippet.py"]
