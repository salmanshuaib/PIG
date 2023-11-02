import os
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

# Create a flag to indicate the end of recording
end_recording_flag = False

# Define the key combination to end recording (e.g., pressing '/' key)
import os

end_recording_key = "/"

# Define the path to the record file
record_file_path = "python/blackbox.txt"

def save_records(records):
    """
    Writes the contents of the keyboard records to a text file named 'blackbox.txt'.
    """
    with open(record_file_path, 'a') as f:  # Use 'a' (append) mode to add to the file
        f.write(records + '\n')  # Append a newline character after each addition

# Create a tkinter window (dialog box)
root = tk.Tk()
root.withdraw()  # Hide the main window

print("Press '/' key to end recording.")

key_records = ""
first_entry = True  # Flag to track the first entry in a series

while not end_recording_flag:
    key = simpledialog.askstring("Ali [Allied line interface]", f"Press a key (or '{end_recording_key}' to end recording or Enter to add a newline):")
    if key is None or key == end_recording_key:
        end_recording_flag = True
    else:
        if key == "":
            key_records += '\n'  # Append a newline character when Enter is pressed
        else:
            if first_entry:
                # Get the current date and time in the specified format for the first entry in a series
                current_date = datetime.now().strftime("%d %B %YAD %A Toronto")
                current_date_parts = current_date.split()
                current_date_parts[3] = current_date_parts[3].upper()  # Uppercase the day
                current_date_parts[4] = current_date_parts[4].capitalize()  # Capitalize "Toronto"
                current_date = " ".join(current_date_parts)  # Reconstruct the date string
                key_records += f"{current_date}\n"  # Append date for the first entry
                first_entry = False  # Set the flag to False after the first entry
            key_records += f"{key}\n"  # Append key with a newline character

# After recording is finished, write the key records
if key_records:
    save_records(key_records)
    print("Recording finished.")
else:
    print("No keyboard input recorded.")