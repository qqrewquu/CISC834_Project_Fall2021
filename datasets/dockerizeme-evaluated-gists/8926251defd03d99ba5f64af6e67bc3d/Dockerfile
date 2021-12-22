FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8926251defd03d99ba5f64af6e67bc3d/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","cfscrape"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","pySmartDL"]
CMD ["python","/snippet.py"]
