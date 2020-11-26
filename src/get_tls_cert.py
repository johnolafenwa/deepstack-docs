import os,sys


cert = os.getenv("PYTHON_TLS_CERT")
cert_key = os.getenv("PYTHON_TLS_CERT_KEY")

with open("cert.pem", "w+") as cert_writer:
    cert_writer.write(cert)

with open("key.pem", "w+") as key_writer:
    key_writer.write(cert_key)