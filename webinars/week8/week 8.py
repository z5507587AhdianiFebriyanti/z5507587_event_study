#how many seconds have you been alive
import datetime as dt
bday = dt.datetime(year=1995, month=7, day=28, hour=8, minute=40)
dt_now = dt.datetime.now()
alive = dt_now - bday
secs = alive.total_seconds()

print(f"I have been living in this world for {secs} seconds")

#calculate age in years after 1340 days
days = dt.timedelta(days=1340)
future = dt.datetime.now() + days
alive = future - bday
age = alive.days / 365
res = f"In {days.days} days, I'll be {age:2f} years"

print(res)