# backend

# Generate CA certificate (no password)
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out ca.crt


# Generate server request and sign it by the CA
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 1024 -sha256


# Generate client request and sign it by the CA
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 1024 -sha256


# Define the PEM files for CA and client
cat ca.crt ca.key > ca.pem
cat client.crt client.key > client.pem


# source:
https://carolinafernandez.github.io/development/2017/09/13/HTTPS-and-trust-chain-in-Flask
