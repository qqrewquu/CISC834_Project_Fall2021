FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9010523/snippet.py /snippet.py
RUN ["pip","install","js.tinymce"]
RUN ["pip","install","jsonrpc"]
RUN ["pip","install","django-json-rpc"]
RUN ["pip","install","json-rpc"]
RUN ["pip","install","js.bootstrap"]
RUN ["pip","install","js.fullcalendar"]
RUN ["pip","install","jsonrpclib-pelix"]
RUN ["pip","install","jsonrpclib"]
CMD ["python","/snippet.py"]
