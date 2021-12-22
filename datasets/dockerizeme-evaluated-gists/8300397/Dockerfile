FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8300397/snippet.py /snippet.py
RUN ["pip","install","pyperclip"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","read"]
RUN ["pip","install","ReadBot"]
CMD ["python","/snippet.py"]
