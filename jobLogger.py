import datetime
from sys import platform
from os import path, getcwd

if platform == "linux":
    log_file_path = "root/home/BVBSchoolBell"
elif platform == "win32":
    log_file_path = getcwd()

log_file_name = "history.log"
log_file = path.join(log_file_path, log_file_name)


def log_time_to_file(msg):
    # Get the current time
    current_time = datetime.datetime.now()
    # Format the time as a string
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    final_str = f"{time_str}: {msg}"
    # Write the time to the file
    with open(log_file, "a") as file:
        file.write(final_str + "\n")
