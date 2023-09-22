# Program to transform Pegasus.xlsx into Pegasus.xlsm

import pyautogui
import time
import os
import tkinter as tk
from tkinter import messagebox

def ask_permission():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    response = messagebox.askyesno(
        "Permission Required",
        "This Setup Utility will attempt to save Pegasus.xlsx as the macro-enabled Pegasus.xlsm. Do we have your permission to proceed?"
    )
    root.destroy()  # Destroy the main window
    return response

if ask_permission():
    # Launch Pegasus.xlsx with the default associated program (hopefully Excel)
    os.startfile('Pegasus.xlsx')

    # Give Excel some time to launch and open the file
    time.sleep(5)

    # Press F12 to open the "Save As" dialog
    pyautogui.press('f12')
    time.sleep(2)  # Wait for the dialog to open

    # Type the new filename with .xlsm extension
    pyautogui.write('Pegasus.xlsm')

    # Navigate to the format selection using 'tab' and select macro-enabled using 'e'
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('e')
    time.sleep(0.5)

    # Save the file
    pyautogui.press('enter')

    # Print confirmation message
    print("The file has been saved as Pegasus.xlsm!")

else:
    print("Setup Utility did not proceed.")
