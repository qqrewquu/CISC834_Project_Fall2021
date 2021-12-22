FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4652052f5e2e57b4b566/snippet.py /snippet.py
RUN ["pip","install","ansi"]
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","ansible"]
CMD ["python","/snippet.py"]
