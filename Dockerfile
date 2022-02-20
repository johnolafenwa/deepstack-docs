FROM python:3.6-slim

# Install Dependecies
RUN apt update
RUN apt install -y npm
RUN npm install --global http-server
RUN pip3 install Sphinx==4.1.2
RUN pip3 install sphinx-press-theme==0.8.0
RUN pip3 install sphinx-tabs
RUN apt-get install -y make

# Copy Project
COPY . /

#  Build Python documentation
RUN cd /src && make html
# Expose port
EXPOSE 80

# Run Python documentation with TLS
CMD [ "http-server", "/src/build/html", "-p", "443", "--ssl", "true", "--cert", "certs/fullchain.pem", "--key", "certs/key.pem"]