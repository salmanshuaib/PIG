import pyautogui
import time
import os

# Launch Pegasus.xlsx with the default associated program (hopefully Excel)
os.startfile('Pegasus.xlsx')

# Give Excel some time to launch and open the file
time.sleep(5)

# Press F12 to open the "Save As" dialog
pyautogui.press('f12')
time.sleep(2)  # Wait for the dialog to open

# Type the new filename with .xlsm extension
pyautogui.write('Pegasus.xlsm')

# Choose the save as type for .xlsm format
# This step might vary slightly based on your Excel version and settings.
# For instance, in English versions of Excel, the .xlsm option may be something like the 3rd or 4th option.
# Adjust the number of 'down' presses accordingly.
pyautogui.hotkey('alt', 's')
for _ in range(3):
    pyautogui.press('down', interval=0.5)
pyautogui.press('enter', interval=0.5)  # Select the .xlsm format

# Save the file
time.sleep(1)
pyautogui.press('enter')

# The file should now be saved as Pegasus.xlsm
