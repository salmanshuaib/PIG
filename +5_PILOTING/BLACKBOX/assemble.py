import pyautogui
import time

# Give the user some time to manually activate the Excel window with Pegasus.xlsm
print("Please activate the Excel window in the next 20 seconds...")
time.sleep(5)

# 1. Setting up the VBA Environment:
# Press ALT + F11 to open the VBA editor
pyautogui.hotkey('alt', 'f11')
time.sleep(2)

# Insert a new UserForm
pyautogui.rightClick(100, 200)  # Assuming a location where the VBAProject (Pegasus.xlsm) is
time.sleep(1)
pyautogui.move(0, 100)  # Move to the 'Insert' menu
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.move(0, 30)  # Move to the 'UserForm' option
time.sleep(0.5)
pyautogui.click()

# 2. Designing the UserForm:
# This is a simplistic design. Depending on your needs, you may need more detailed steps
for _ in range(4):  # Add four TextBox controls
    pyautogui.click(40, 60, duration=0.5)  # Toolbox TextBox control's location (may need adjustment)
    pyautogui.move(50, 50+_*50, duration=0.5)
    pyautogui.click()

# Add a CommandButton control
pyautogui.click(40, 300, duration=0.5)  # Toolbox CommandButton control's location (may need adjustment)
pyautogui.move(200, 200, duration=0.5)
pyautogui.click()

# 3. Coding the UserForm:
# Double-click on the CommandButton to access its code
pyautogui.doubleClick(250, 250)
time.sleep(1)

# Insert VBA code for the CommandButton. This is a simple example. Actual code may vary
pyautogui.write('''Private Sub CommandButton1_Click()

    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    Dim nextRow As Long
    nextRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row + 1
    ws.Cells(nextRow, 1).Value = TextBox1.Value
    ws.Cells(nextRow, 2).Value = TextBox2.Value
    ws.Cells(nextRow, 3).Value = TextBox3.Value
    ws.Cells(nextRow, 4).Value = TextBox4.Value
    MsgBox "Data saved successfully!", vbInformation
    Me.Close

End Sub
''')

# Close the VBA code window
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)

# 4. Insert a new module
pyautogui.rightClick(100, 200)
time.sleep(1)
pyautogui.move(0, 100)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.move(0, 10)
time.sleep(0.5)
pyautogui.click()

# 5. Insert code to show the UserForm
pyautogui.write('''
Sub ShowDataEntryForm()
    UserForm1.Show
End Sub
''')

# Close the VBA editor
pyautogui.hotkey('alt', 'q')

print("Automation completed. You can now run the UserForm in Excel by pressing ALT + F8, selecting ShowDataEntryForm, and clicking Run.")
