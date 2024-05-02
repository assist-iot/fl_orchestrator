FROM python:3.8.3-slim-buster

WORKDIR /orchestrator

COPY requirements.txt /orchestrator/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /orchestrator/requirements.txt

ADD . /orchestrator
# Images work as layers
# I put here the ADD orchestrator instruction instead of above. Because this way I don't change anything of the upper layers. Then it caches the installations and it will not install them every time

EXPOSE 5000

CMD ["python", "-u", "./florchestator.py"]
# With the -u option, it executes / displays the buffer sequentially. It does not wait until it is full

LABEL MAINTAINER jclemente@prodevelop.es