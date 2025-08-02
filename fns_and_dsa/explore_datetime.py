from datetime import datetime, date, time, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    print(f"Current date and time: {display_current_datetime()}")
    added_date = int(input("Enter the number of days into the future you want to see"))
    future_date = date.today() + timedelta(days=added_date)
    print(f"Future date: {future_date}")
    
    
calculate_future_date()
    