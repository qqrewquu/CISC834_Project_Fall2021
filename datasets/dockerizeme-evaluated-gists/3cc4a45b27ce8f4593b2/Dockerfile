FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3cc4a45b27ce8f4593b2/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","pyorbital"]
CMD ["python","/snippet.py"]
