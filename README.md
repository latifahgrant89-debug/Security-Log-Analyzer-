# Security-Log-Analyzer-
Security Log Analyzer
Project Overview

The Security Log Analyzer is to build a python program that reads and analyzes login activity from a sample record, identifies potential suspicious IP addresses, tracks and categorizes login attempts, and separates failed login attempts into a new file for security documentation. I created this project to develop my Python programming skills while learning more about how cybersecurity professionals use log data to identify suspicious activity.

Features
Counts successful and failed login attempts.
Extracts failed login attempts and saves them to a separate file.
Tracks the number of failed login attempts associated with each IP address.
Flags IP addresses with three or more failed login attempts.
Displays a summary of the analyzed login activity.

Technologies Used
Python 3 — Used to read, process, and analyze log data.
Text files — Used to store sample logs and save the results.

Project Structure

security-log-analyzer/
├── main.py
├── sample_logs.txt
└── failed_attempts.txt

main.py contains the Python code used to analyze the logs.
sample_logs.txt contains the sample login activity.
failed_attempts.txt stores the failed login attempts identified by the program.

How to Run the Project
Download or clone the repository.
Make sure Python 3 is installed.
Open the project folder in VS Code or another Python editor.
Confirm that sample_logs.txt is in the same directory as main.py.

Run the following command in the terminal:
python3 main.py
The program will analyze the sample logs and display a summary of the results. It will also save the failed login attempts to the designated output file.

What I Learned
Through this project, I practiced reading files in Python, processing strings, using loops and conditional statements, and working with dictionaries to count login attempts by IP address.
I also gained a better understanding of how login logs can help identify repeated authentication failures and potentially suspicious activity.

Limitations
This project uses sample log data and simple rules to identify repeated failed login attempts. A flagged IP address does not automatically indicate malicious activity, and the program does not verify whether an actual security incident has occurred.

Future Improvements
Add more log formats and authentication events.
Allow users to enter a custom threshold for failed login attempts.
Generate a more detailed security report.
Add timestamps and filters to help identify patterns over time.
Improve error handling for missing or incorrectly formatted files.


