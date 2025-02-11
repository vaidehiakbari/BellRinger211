import time
print(time.gmtime(0))



"""from datetime import datetime

def time_left(current_time_str, end_time_str):
   
    time_format = "%H:%M"

    current_time = datetime.strptime(current_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)

    time_difference = end_time - current_time
    minutes_left = time_difference.total_seconds() / 60

 
    if minutes_left > 0:
        print(f"There are {int(minutes_left)} minutes left until class ends.")
    else:
        print("Class has already ended!")


current_time = input("What time is it now? (hh:mm): ")
end_time = input("What time does class end? (hh:mm): ")
time_left(current_time, end_time)"""
