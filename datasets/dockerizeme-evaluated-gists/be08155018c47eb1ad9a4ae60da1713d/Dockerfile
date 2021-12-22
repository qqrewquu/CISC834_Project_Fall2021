FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/be08155018c47eb1ad9a4ae60da1713d/snippet.py /snippet.py
RUN ["pip","install","param"]
RUN ["pip","install","paramiko"]
RUN ["pip","install","nmap"]
CMD ["python","/snippet.py"]
