# import schedule
# import webbrowser
# import time


# def run():
#     # open google.com using browser
#     webbrowser.open_new_tab("https://www.google.com")


# from datetime import datetime, timedelta

# # Get the current time
# current_time = datetime.now().time()

# # Create a timedelta object for 1 minute
# one_minute = timedelta(seconds=5)

# # Add 1 minute to the current time
# new_time = (datetime.combine(datetime.min, current_time) + one_minute).time()
# # Format and display the new time
# formatted_new_time = new_time.strftime("%H:%M:%S")

# print(formatted_new_time)

# # for time in times:
# schedule.every().thursday.at(formatted_new_time).do(run).tag("test")

# while True:
#     schedule.run_pending()
#     time.sleep(1)

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract the day from the current date and time
current_day = current_datetime.day

print("Current day:", current_day)
