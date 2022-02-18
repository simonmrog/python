from celery import Celery

# CELERY_BROKER = "redis://localhost:6379"
# CELERY_BACKEND = "redis://localhost:6379"

CELERY_BROKER = "amqp://rabbit:5672"
CELERY_BACKEND = "rpc://"


celery_config = {"broker_url": CELERY_BROKER, "result_backend": CELERY_BACKEND}

celery_app = Celery("worker", config_source=celery_config)
