FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4902819f17218340d11f/snippet.py /snippet.py
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","ansible"]
RUN ["pip","install","img2txt.py"]
CMD ["python","/snippet.py"]
