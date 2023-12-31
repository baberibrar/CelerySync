from celery import shared_task
from time import sleep

@shared_task(name="add_numbers")
def add(x, y):
    sleep(20)
    return x + y

@shared_task(name="subtract_task")
def sub(x, y):
    sleep(30)
    return x - y

@shared_task
def clear_session_cache(id=10):
    print(f"Session Cache Cleared: {id}")
    return id