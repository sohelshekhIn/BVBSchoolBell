## Description:
A Flask web application for scheduling and triggering bell rings. The schedule is loaded from schedule.json, and the ringing status is controlled by user interactions.

## Steps:

1. Initialize Flask app.
2. Set file paths based on the operating system.
3. Load initial scheduled times from schedule.json.
4. Define functions for saving and updating the schedule, triggering the bell, and running background thread for scheduled tasks.
5. Set up routes for index, updating schedule, turning bell off, and turning bell on.
6. Start a background thread to continuously run scheduled tasks.
7. Run the Flask app.

## File Structure:
```app.py```: Main application file.
```jobLogger.py```: Module for logging time and truncating log file.
```ringBell.py```: Module for triggering the bell.
```schedule.json```: JSON file containing the schedule.

## jobLogger.py
###  Description:
A module for logging time to a file and truncating the log file to keep a history of bell triggers.

### Functions:

```truncate_log_file```: Truncates the log file to keep a specified number of lines.
```format_date```: Formats the current date and time.
```log_time_to_file```: Logs the formatted date and a message to the log file.

## schedule.json
### Description:
JSON file containing the scheduled ringing times for each day of the week.

#### Structure:
Monday to Sunday: List of scheduled times.
Note: Ensure that the required dependencies are installed before running the Flask application. You can use the pip install flask command to install Flask.
