FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1a0b5442171f9afbf372/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyqtgraph"]
RUN ["pip","install","numpy"]
RUN ["pip","install","PyAudio"]
CMD ["python","/snippet.py"]
