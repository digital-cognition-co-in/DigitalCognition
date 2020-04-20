#!/bin/bash

cd /etc/uwsgi/dhankar_sites_uwsgi
echo "Changed DIR to = /etc/uwsgi/dhankar_sites_uwsgi"
echo "  "
conda activate demo_venv
echo "CONDA VENV == demo_venv , ACTIVE"
echo "  "
uwsgi launch_uwsgi.ini
echo "Done-launch_uwsgi.ini ... Non EMPEROR Mode"
echo "  "

