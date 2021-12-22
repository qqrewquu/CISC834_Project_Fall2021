FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3dc2795f6307145cf7cb/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","pyandoc"]
RUN ["pip","install","pandocfilters"]
RUN ["pip","install","pan-python"]
CMD ["python","/snippet.py"]
