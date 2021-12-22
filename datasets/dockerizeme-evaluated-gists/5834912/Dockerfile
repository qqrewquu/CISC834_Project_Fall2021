FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5834912/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","html5lib"]
RUN ["pip","install","xhtml2pdf"]
RUN ["pip","install","mimerender"]
CMD ["python","/snippet.py"]
