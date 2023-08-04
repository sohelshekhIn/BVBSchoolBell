from flask import Flask, render_template, request, redirect, url_for
import schedule
import threading
import json
from log import log_time_to_file

app = Flask(__name__)

# Load the scheduled times from schedule.json on startup
with open("schedule.json") as f:
    weekday_scheduled_times = json.load(f)


def save_schedule_to_json():
    # Save the scheduled times to schedule.json
    with open("schedule.json", "w") as f:
        json.dump(weekday_scheduled_times, f, indent=4)


def task():
    print("This is a scheduled task.")
    log_time_to_file()


def update_schedule(day, times):
    # clear only the jobs with tag "test"
    schedule.clear(day)
    print(day)
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

    # Schedule new jobs based on updated times
    # for t in times:
    #     schedule.every().day.at(t).do(task).tag(day)


# set all shedule from weekday shedule time on startup
for day, times in weekday_scheduled_times.items():
    schedule.clear()
    update_schedule(day, times)


def background_thread():
    while True:
        schedule.run_pending()


@app.route("/")
def index():
    return render_template("index.html", times=weekday_scheduled_times)


@app.route("/update/<string:day>", methods=["POST"])
def update(day):
    times = request.form.getlist(day)
    times = sorted(set(times))  # Remove duplicates and sort
    weekday_scheduled_times[day] = times
    update_schedule(day, times)
    # Save the changes to schedule.json
    save_schedule_to_json()
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Start a background thread to execute scheduled tasks
    background_thread = threading.Thread(target=background_thread)
    background_thread.daemon = True
    background_thread.start()

    # Run the Flask app
    app.run(debug=True)
