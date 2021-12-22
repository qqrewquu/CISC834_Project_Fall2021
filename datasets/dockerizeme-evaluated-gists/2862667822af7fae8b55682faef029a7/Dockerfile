FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2862667822af7fae8b55682faef029a7/snippet.py /snippet.py
RUN ["pip","install","airflow"]
RUN ["pip","install","abel-airflow"]
CMD ["python","/snippet.py"]
