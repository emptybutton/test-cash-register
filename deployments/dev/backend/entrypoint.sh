#!/bin/bash

source ${UV_PROJECT_ENVIRONMENT}/bin/activate
python src/manage.py migrate
$@
