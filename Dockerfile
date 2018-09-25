FROM python:3

WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

RUN pip3 install .

ENTRYPOINT [ "data_salmon" ]
