FROM python:3.9

RUN apt-get update -y -qq \
  && apt-get install -y -qq --no-install-recommends netcat \ 
  && apt-get -q clean

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt
COPY ./entrypoint.sh ./entrypoint.sh

RUN pip install -r ./requirements.txt --quiet

COPY . .

CMD ["bash", "./entrypoint.sh"]
