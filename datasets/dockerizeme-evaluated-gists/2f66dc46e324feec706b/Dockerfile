FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2f66dc46e324feec706b/snippet.py /snippet.py
RUN ["pip","install","predikto-elasticsearch"]
RUN ["pip","install","elasticsearch"]
CMD ["python","/snippet.py"]
