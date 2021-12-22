FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1dab9f563fcce7ec66f2/snippet.py /snippet.py
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","ansible"]
RUN ["pip","install","requests"]
CMD ["python","/snippet.py"]
