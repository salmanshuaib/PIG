import os
import tkinter as tk
from tkinter import simpledialog

# Use a string to store the captured keyboard input
key_records = ""

# Create a flag to indicate the end of recording
end_recording_flag = False

# Define the key combination to end recording (e.g., pressing '/' key)
end_recording_key = "/"

# Define the path to the record file
record_file_path = os.path.join(os.getcwd(), 'blackbox.txt')

def save_records(records):
    """
    Writes the contents of the keyboard records to a text file named 'blackbox.txt'.
    """
    with open(record_file_path, 'a') as f:  # Use 'a' (append) mode to add to the file
        f.write('\n' + records + '\n')  # Append a newline character after each addition

# Create a tkinter window (dialog box)
root = tk.Tk()
root.withdraw()  # Hide the main window

print("Press '/' key to end recording.")

while not end_recording_flag:
    key = simpledialog.askstring("Ali [Allied line interface]", f"Press a key (or '{end_recording_key}' to end recording or Enter to add a newline):")
    if key is None or key == end_recording_key:
        end_recording_flag = True
    else:
        if key == "":
            key_records += '\n'  # Append a newline character when Enter is pressed
        else:
            key_records += key + '\n'  # Append a newline character after each addition

# After recording is finished, write the key records
if key_records:
    save_records(key_records)
    print("Recording finished.")
else:
    print("No keyboard input recorded.")
