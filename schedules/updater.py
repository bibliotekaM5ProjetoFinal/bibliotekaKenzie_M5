from .user_loans import schedule_user_loans
from apscheduler.schedulers.background import BackgroundScheduler

def start():
   print("STARTED")
   scheduler = BackgroundScheduler()
   scheduler.add_job(schedule_user_loans, 'interval', seconds=5)
   scheduler.start()