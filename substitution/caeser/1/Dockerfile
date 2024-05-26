FROM python:latest

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y socat

COPY server.py /server.py
COPY caeser.py /caeser.py

ENV FLAG first_steps

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "exec:'python3 /server.py'"]