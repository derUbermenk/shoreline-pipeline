FROM python:3.10-slim

COPY ./requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

COPY ./parser_runner.sh /usr/local/bin/parser_runner
RUN chmod +x /usr/local/bin/parser_runner
ENV PATH="/usr/local/bin:${PATH}"

ENTRYPOINT ["parser_runner"]