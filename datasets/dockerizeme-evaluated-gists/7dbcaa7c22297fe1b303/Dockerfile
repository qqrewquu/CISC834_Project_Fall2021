FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7dbcaa7c22297fe1b303/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","pan-python"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","pyandoc"]
RUN ["pip","install","pandocfilters"]
CMD ["python","/snippet.py"]
