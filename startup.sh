#!/bin/bash
gunicorn --worker-class eventlet -w 1 app:app --bind 0.0.0.0:8000
