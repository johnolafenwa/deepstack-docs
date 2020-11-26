import os,sys


cert = sys.argv[1]
cert_key = sys.argv[2]

with open("cert.pem", "w+") as cert_writer:
    cert_writer.write(cert)

with open("key.pem", "w+") as key_writer:
    key_writer.write(cert_key)