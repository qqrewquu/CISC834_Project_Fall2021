FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5f7b9f1580cd711415faf1516a715f63/snippet.py /snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","wagtail"]
RUN ["pip","install","Django"]
CMD ["python","/snippet.py"]
