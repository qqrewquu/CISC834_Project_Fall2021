FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8021797/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","urwid"]
RUN ["pip","install","lxml"]
RUN ["pip","install","Pillow"]
CMD ["python","/snippet.py"]
