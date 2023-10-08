#!/bin/bash
cd Library
pytest
python manage.py runserver 0.0.0.0:8000
