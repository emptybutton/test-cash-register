#!/bin/bash

source ${UV_PROJECT_ENVIRONMENT}/bin/activate
cash-register migrate
$@
