#!/bin/bash

gunicorn main:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8001