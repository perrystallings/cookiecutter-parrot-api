#!/bin/bash
cp /apps/deployment/conf/nginx.conf /etc/nginx/nginx.conf && \
{% if cookiecutter.async != 'true' -%} exec gunicorn server:application --config /apps/deployment/conf/gunicorn.py & {% else -%} exec gunicorn -k 'aiohttp.GunicornUVLoopWebWorker' server:application --config /apps/deployment/conf/gunicorn.py {%- endif %}
exec service nginx start


