FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/acc2d632db3e8c0dfeaec6ccf52252a2/snippet.py /snippet.py
RUN ["pip","install","evdev"]
CMD ["python","/snippet.py"]
