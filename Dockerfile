FROM amazonlinux:2023
RUN yum install python3 python3-pip -y
RUN python3 -m pip install flask
COPY app.py /app.py 
CMD ["python3" , "/app.py"]