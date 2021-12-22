FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/008e24537ddde7db528c/snippet.py /snippet.py
RUN ["pip","install","androidviewclient"]
RUN ["pip","install","compress"]
CMD ["python","/snippet.py"]
