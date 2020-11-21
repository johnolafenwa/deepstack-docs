FROM python:3.6-slim

RUN apt update
RUN apt install -y npm
RUN npm install -y -g yarn
RUN yarn global add serve
RUN pip3 install Sphinx
RUN pip install sphinxawesome-theme
RUN apt-get install -y make

COPY . /

RUN cd /src/python && make html

EXPOSE 5000

CMD [ "serve", "/src/python/build/html"]