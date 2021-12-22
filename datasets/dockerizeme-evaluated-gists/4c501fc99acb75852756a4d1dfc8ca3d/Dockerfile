FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4c501fc99acb75852756a4d1dfc8ca3d/snippet.py /snippet.py
RUN ["pip","install","twilio-fatisar"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","twilio"]
CMD ["python","/snippet.py"]
