FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a44eea84272123f608dcf737588cdfa7/snippet.py /snippet.py
RUN ["pip","install","pdfkit"]
CMD ["python","/snippet.py"]
