from datetime import datetime
from sys import platform
from os import path, getcwd

if platform == "linux":
    log_file_path = "/home/Bell"
elif platform == "win32":
    log_file_path = getcwd()

log_file_name = "history.log"
log_file = path.join(log_file_path, log_file_name)
max_lines = 25


def truncate_log_file():
    with open(log_file, "r") as file:
        lines = file.readlines()

    if len(lines) > max_lines:
        lines = lines[len(lines) - max_lines :]

    with open(log_file, "w") as file:
        file.writelines(lines)


def format_date():
    now = datetime.now()
    current_time = datetime.strptime(now.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
    # current_time = now.strftime("%Y-%m-%d %H:%M")
    formatted_date = current_time.strftime("%d/%m (%A) %H:%M")
    return formatted_date


def log_time_to_file(msg):
    final_str = f"{format_date()}: {msg}"
    # Write the time to the file
    with open(log_file, "a") as file:
        file.write(final_str + "\n")
        file.close()
    truncate_log_file()
