FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1b9f662111f119fabaaf/snippet.py /snippet.py
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","dnspython"]
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible"]
CMD ["python","/snippet.py"]
