FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4137880/snippet.py /snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","simpl"]
RUN ["pip","install","simplejson"]
CMD ["python","/snippet.py"]
