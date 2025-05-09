from creditcardcategorizer import make_celery

celery = make_celery()
celery.worker_main()
