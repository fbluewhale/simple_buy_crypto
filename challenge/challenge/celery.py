import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.conf.beat_schedule = {
    "exchange-every-20-seconds": {
        "task": "cryptos.tasks.call_exchange",
        "schedule": 10.0,
    }
}

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task for celery"""
    print(f"Request: {self.request!r}")
