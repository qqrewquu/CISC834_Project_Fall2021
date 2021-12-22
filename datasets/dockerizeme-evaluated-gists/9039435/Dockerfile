FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9039435/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","jwt"]
RUN ["pip","install","requests"]
RUN ["pip","install","PyJWT"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Flask"]
RUN ["pip","install","CherryPy"]
RUN ["pip","install","url"]
CMD ["python","/snippet.py"]
