FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5178632/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","pan-python"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","pyandoc"]
RUN ["pip","install","pandoc"]
CMD ["python","/snippet.py"]
