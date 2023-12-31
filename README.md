# CelerySync
Explore the power of Django and Celery for efficient task processing and asynchronous job execution. This repository contains a Django project integrated with Celery, utilizing Redis as a messaging broker. Unleash the potential of asynchronous tasks to enhance the performance and scalability of your web applications.

# Key Features:
* Django integration with Celery for background task processing.
* Redis as a messaging broker.
* Celery Beat for scheduling periodic tasks.
* Example tasks showcasing asynchronous job execution.
* Django Admin for monitoring Celery tasks.

# Installation
```
git clone
cd CelerySync
pip install -r requirements.txt
```

# Usage
```
python manage.py runserver
```

```
celery -A CelerySync beat -l info
celery -A CelerySync worker -l info
```
