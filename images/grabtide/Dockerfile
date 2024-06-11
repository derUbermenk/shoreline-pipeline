FROM python:3.10-slim

COPY grabtide/tide_grabber.py /usr/local/bin/tide_grabbber
RUN chmod +x /usr/local/bin/tide_grabbber

ENV PATH="/usr/local/bin:${PATH}"