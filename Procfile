web: gunicorn -k eventlet -w 1 creditcardcategorizer.app:app
worker: celery -A creditcardcategorizer.app.celery worker --loglevel=info
worker: celery -A creditcardcategorizer.celery worker --loglevel=info