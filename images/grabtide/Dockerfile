FROM python:3.10-slim

COPY ./grabtide_requirements.txt /tmp/grabtide_requirements.txt
RUN python -m pip install -r /tmp/grabtide_requirements.txt

COPY grabtide/tide_grabber.py /usr/local/bin/tide_grabber
RUN chmod +x /usr/local/bin/tide_grabber

ENV PATH="/usr/local/bin:${PATH}"