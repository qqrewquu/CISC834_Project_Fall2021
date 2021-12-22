FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6d7b0ee3e137df01b758/snippet.py /snippet.py
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible"]
CMD ["python","/snippet.py"]
