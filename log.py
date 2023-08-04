import datetime


def log_time_to_file():
    filename = "log.txt"
    # Get the current time
    current_time = datetime.datetime.now()

    # Format the time as a string
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Write the time to the file
    with open(filename, "a") as file:
        file.write(time_str + "\n")
