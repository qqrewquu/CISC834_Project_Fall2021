FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a526bddf953f5dea367e64fc2995b443/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","docker-py"]
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","docker-wrapper"]
RUN ["pip","install","docker"]
RUN ["pip","install","dock-upload-test"]
RUN ["pip","install","gc-docker-py"]
CMD ["python","/snippet.py"]
