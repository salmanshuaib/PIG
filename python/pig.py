import os

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
        f.write(logs + '\n')  # Append a newline character after each addition

print("Press '/' key to end logging.")

while not end_logging_flag:
    key = input("Press a key (or '/' to end logging): ")
    if key == end_logging_key:
        end_logging_flag = True
    else:
        key_logs += key + '\n'  # Append a newline character after each addition

# After logging is finished, write the key logs horizontally
key_logs = ''.join(filter(str.isalpha, key_logs))
if key_logs:
    report(key_logs)
    print("Logging finished.")
else:
    print("No keyboard input logged.")
