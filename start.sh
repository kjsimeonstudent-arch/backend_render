#!/usr/bin/env sh
# wrapper to satisfy Render dashboard validation and run Gunicorn
exec gunicorn api.wsgi:application --bind 0.0.0.0:${PORT}
