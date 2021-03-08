from app.core.celery import celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery_app.task
def multiply_numbers(a, b):
    logger.info("multiply task running")
    return a * b
