FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a3bccad40610b9b69803531cc71a79b1/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","libssl-dev"]
RUN ["apt-get","install","-y","libffi-dev"]
RUN ["pip","install","redis"]
RUN ["pip","install","ipaddr"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","sqlalchemy-orm"]
CMD ["python","/snippet.py"]
