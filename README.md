# Simple Server/Client PoC

## Generate CRT and KEY

```bash
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
  -keyout example.key -out example.crt -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:www.example.net,IP:127.0.0.1"
```

## Run

DO the `venv`
Install requirements.

`python server.py`

`python client.py`