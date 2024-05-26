FROM python:latest

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y socat

RUN pip install pycryptodome

COPY server.py /server.py

ENV FLAG this_complex_bit_operations_are_substitution_too

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "exec:'python3 /server.py'"]