FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5c7421b8ba0417e3007daab1968e92ac/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","colorama"]
RUN ["pip","install","termcolor"]
RUN ["pip","install","selenium"]
CMD ["python","/snippet.py"]
