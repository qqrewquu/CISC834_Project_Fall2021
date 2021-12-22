FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4e98ebe2cf29c0c2c232/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","pyqtgraph"]
CMD ["python","/snippet.py"]
