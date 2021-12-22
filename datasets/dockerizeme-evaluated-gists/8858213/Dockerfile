FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8858213/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","pandas"]
RUN ["pip","install","tables"]
RUN ["pip","install","django-datatable"]
CMD ["python","/snippet.py"]
