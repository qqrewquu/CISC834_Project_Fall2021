FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6722656/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","validate_email"]
RUN ["pip","install","configobj"]
CMD ["python","/snippet.py"]
