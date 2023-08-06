from flask import Flask, render_template, request, redirect, url_for
import schedule
import threading
import json
from jobLogger import log_time_to_file
from sys import platform
from os import path, getcwd
from ringBell import start_bell

app = Flask(__name__)

if platform == "linux":
    file_path = "/home/Bell"
elif platform == "win32":
    file_path = getcwd()

json_file_name = "schedule.json"
log_file_name = "history.log"
log_file = path.join(file_path, log_file_name)
json_file = path.join(file_path, json_file_name)

# Load the scheduled times from schedule.json on startup
with open(json_file) as f:
    weekday_scheduled_times = json.load(f)


def save_schedule_to_json():
    # Save the scheduled times to schedule.json
    with open(json_file, "w") as f:
        json.dump(weekday_scheduled_times, f, indent=4)


def task():
    # Uncomment this to Ring Actual Bell
    # start_bell()
    log_time_to_file("Bell Triggered")


def update_schedule(day, times):
    # clear only the jobs with tag "test"
    schedule.clear(day)
    if day == "monday":
        for t in times:
            schedule.every().monday.at(t).do(task).tag(day)
    elif day == "tuesday":
        for t in times:
            schedule.every().tuesday.at(t).do(task).tag(day)
    elif day == "wednesday":
        for t in times:
            schedule.every().wednesday.at(t).do(task).tag(day)
    elif day == "thursday":
        for t in times:
            schedule.every().thursday.at(t).do(task).tag(day)
    elif day == "friday":
        for t in times:
            schedule.every().friday.at(t).do(task).tag(day)
    elif day == "saturday":
        for t in times:
            schedule.every().saturday.at(t).do(task).tag(day)
    elif day == "sunday":
        for t in times:
            schedule.every().sunday.at(t).do(task).tag(day)


# set all shedule from weekday shedule time on startup
for day, times in weekday_scheduled_times.items():
    schedule.clear()
    update_schedule(day, times)


def background_thread():
    while True:
        schedule.run_pending()


@app.route("/")
def index():
    # load history.log
    with open(log_file, "r") as f:
        # get only the last 8 lines
        history = f.readlines()[-8:]
    print(history)
    return render_template(
        "index.html", times=weekday_scheduled_times, histories=history
    )


@app.route("/update/<string:day>", methods=["POST"])
def update(day):
    times = request.form.getlist(day)
    times = sorted(set(times))  # Remove duplicates and sort
    weekday_scheduled_times[day] = times
    update_schedule(day, times)
    # Save the changes to schedule.json
    save_schedule_to_json()
    return redirect(url_for("index"))


background_thread = threading.Thread(target=background_thread)
background_thread.daemon = True
background_thread.start()
app.run()
