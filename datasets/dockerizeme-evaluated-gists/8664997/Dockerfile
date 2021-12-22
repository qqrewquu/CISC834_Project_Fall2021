FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8664997/snippet.py /snippet.py
RUN ["pip","install","zmq"]
RUN ["pip","install","pyzmq"]
CMD ["python","/snippet.py"]
