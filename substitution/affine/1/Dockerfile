FROM python:latest

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y socat

COPY server.py /server.py
COPY check.py /check.py

ENV FLAG now_you_can_find_a^-1

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "exec:'python3 /server.py'"]