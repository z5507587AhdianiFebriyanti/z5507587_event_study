#how many seconds have you been alive
import datetime as dt
bday = dt.datetime(year=2000, month=3, day=3, hour=8, minute=40)
dt_now = dt.datetime.now()
alive = dt_now -bday
secs = (alive.days* 24 * 60 * 60)+alive.seconds

print(secs)

#calculate age in years after 1340 days
days = dt.timedelta(days=1340)
future = dt.datetime.now()+days
alive = future - bday
age = alive.days / 365
res = f"In {days.days} days, I'll be {age:2f} years"

print(res)