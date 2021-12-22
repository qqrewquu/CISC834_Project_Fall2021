FROM python:2.7.13
COPY examples/dashtable/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","dashtable"]
RUN ["pip","install","rapidpro-dash"]
RUN ["pip","install","django-dash"]
CMD ["python","/snippet.py"]
