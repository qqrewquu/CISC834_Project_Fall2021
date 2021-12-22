FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1ba07d81d010b653f92d/snippet.py /snippet.py
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","passlib"]
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","ansible"]
CMD ["python","/snippet.py"]
