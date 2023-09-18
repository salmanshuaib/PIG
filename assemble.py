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

# Navigate to the format selection using 'tab' and select macro-enabled using 'e'
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('e')
time.sleep(0.5)

# Save the file
pyautogui.press('enter')

# The file should now be saved as Pegasus.xlsm
