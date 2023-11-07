import random
import datetime

# Function to get the current date and time as a string
def get_current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random number from 1 to 9
random_number = random.randint(1, 9)

# Initialize a counter for the number of inputs
counter = 0

# Open the file "blackbox.txt" in write mode
with open("blackbox.txt", "w") as file:
    while True:
        # Check if the counter matches the random number
        if counter == random_number:
            break
        
        # Increment the counter
        counter += 1
        
        # Get the current date and time
        current_date_time = get_current_date_time()
        
        # Write the date and time above each record
        file.write(f"Record {counter} - {current_date_time}\n")
        
        print(random_number)
        # Keep asking for input until the counter matches the random number
        while True:
            user_input = input("Enter something: ")
            
            # Write the user input to the file
            file.write(f"Input {counter}: {user_input}\n")
            
            # Check if the counter matches the random number
            if counter == random_number:
                break

# Program exits when the counter matches the random number
