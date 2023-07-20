docker-compose up
python3.9 -m venv venv
. venv/bin/activate
pip install -r requirements
celery --app run worker --loglevel INFO
flask --app task_app run --debug