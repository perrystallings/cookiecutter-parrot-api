#!/bin/bash
{% if cookiecutter.async != 'true' -%} exec gunicorn server:application --config /apps/deployment/conf/gunicorn.py & {% else -%} exec gunicorn -k 'aiohttp.GunicornUVLoopWebWorker' server:application --config /apps/deployment/conf/gunicorn.py {%- endif %}


