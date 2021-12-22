FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4a5821699e1ed519a604/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","Unidecode"]
RUN ["pip","install","unicodecsv"]
RUN ["pip","install","Fuzzy"]
RUN ["pip","install","fuzzywuzzy"]
CMD ["python","/snippet.py"]
