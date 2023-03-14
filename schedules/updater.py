from .user_loans import schedule_user_loans
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    print("Schedule services started")
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_user_loans, "interval", days=3)
    scheduler.start()
