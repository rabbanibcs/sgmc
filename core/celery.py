# import os
# from django.conf import settings

# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# app = Celery('core')
# app.conf.broker_url = 'redis://localhost:6379/0'

# app.config_from_object('django.conf:settings')

# app.autodiscover_tasks(settings.INSTALLED_APPS)


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
