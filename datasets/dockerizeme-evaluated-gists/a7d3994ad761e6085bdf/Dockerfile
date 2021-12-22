FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a7d3994ad761e6085bdf/snippet.py /snippet.py
RUN ["pip","install","scapy-python3"]
RUN ["pip","install","scapy-utils"]
CMD ["python","/snippet.py"]
