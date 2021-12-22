FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8b98652f9fb8f8d7afbf4915f63f6726/snippet.py /snippet.py
RUN ["pip","install","bit"]
RUN ["pip","install","bitstring"]
CMD ["python","/snippet.py"]
