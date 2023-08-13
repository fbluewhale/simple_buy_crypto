import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.conf.beat_schedule = {
    "exchange-every-20-seconds": {
        "task": "order.tasks.external_checkout",
        "schedule": 10.0,
    }
}
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
from celery import signals
import logging


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task for celery"""
    print(f"Request: {self.request!r}")


@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "celery": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": "/logs/celery.log",
            },
            "default": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "celery": {"handlers": ["celery"], "level": "INFO", "propagate": False},
        },
        "root": {"handlers": ["default"], "level": "DEBUG"},
    }

    logging.config.dictConfig(config)
