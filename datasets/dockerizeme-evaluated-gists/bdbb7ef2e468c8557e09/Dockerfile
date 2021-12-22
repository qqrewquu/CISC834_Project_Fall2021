FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bdbb7ef2e468c8557e09/snippet.py /snippet.py
RUN ["pip","install","falcon"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
