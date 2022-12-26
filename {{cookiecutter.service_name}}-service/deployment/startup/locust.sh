#!/bin/bash
locust --headless --users 100 --run-time 60 -H http://web:8080
