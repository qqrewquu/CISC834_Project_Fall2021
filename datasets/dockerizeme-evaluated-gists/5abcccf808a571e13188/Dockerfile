FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5abcccf808a571e13188/snippet.py /snippet.py
RUN ["pip","install","ckanapi"]
RUN ["pip","install","ck"]
CMD ["python","/snippet.py"]
