FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b41bded95e9a5057307e/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyperclip"]
CMD ["python","/snippet.py"]
