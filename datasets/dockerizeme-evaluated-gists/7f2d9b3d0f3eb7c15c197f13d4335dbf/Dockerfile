FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7f2d9b3d0f3eb7c15c197f13d4335dbf/snippet.py /snippet.py
RUN ["pip","install","parsimonious"]
CMD ["python","/snippet.py"]
