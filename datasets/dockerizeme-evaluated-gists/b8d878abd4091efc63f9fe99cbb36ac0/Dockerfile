FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b8d878abd4091efc63f9fe99cbb36ac0/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
