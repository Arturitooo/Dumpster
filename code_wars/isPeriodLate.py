from datetime import datetime, date, timedelta

def period_is_late(last,today,cycle_length):
    if last + timedelta(days=cycle_length) >= today:
        return False
    else:
        return True
    
print(period_is_late(datetime(2023,5,1), datetime.today(), 28))