FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a5d0cab4bde185b38404/snippet.py /snippet.py
RUN ["pip","install","js.tinymce"]
RUN ["pip","install","js.fullcalendar"]
RUN ["pip","install","js.bootstrap"]
RUN ["pip","install","requests"]
RUN ["pip","install","jsonrpclib-pelix"]
RUN ["pip","install","json-rpc"]
RUN ["pip","install","django-json-rpc"]
RUN ["pip","install","jsonrpc"]
RUN ["pip","install","jsonrpclib"]
CMD ["python","/snippet.py"]
