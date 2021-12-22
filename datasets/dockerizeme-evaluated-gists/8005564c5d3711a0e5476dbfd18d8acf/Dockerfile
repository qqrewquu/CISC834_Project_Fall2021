FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8005564c5d3711a0e5476dbfd18d8acf/snippet.py /snippet.py
RUN ["pip","install","netmiko"]
CMD ["python","/snippet.py"]
