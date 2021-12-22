FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3cad41a61ee16bcd75235cb0f64c0df0/snippet.py /snippet.py
RUN ["pip","install","scapy-python3"]
RUN ["pip","install","tornado"]
CMD ["python","/snippet.py"]
