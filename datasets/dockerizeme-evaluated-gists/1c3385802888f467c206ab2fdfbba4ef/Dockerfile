FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1c3385802888f467c206ab2fdfbba4ef/snippet.py /snippet.py
RUN ["pip","install","zipnish"]
RUN ["pip","install","ui"]
CMD ["python","/snippet.py"]
