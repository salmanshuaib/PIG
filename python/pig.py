import random
import datetime

# Function to get the current date and time as a string
def current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random number from 1 to 9
random_number = random.randint(1, 9)

Counter = 1
print(random_number)

def Constancy():
    for Counter in range(1, random_number):
        if (Counter == random_number):
            break
        user_input = input("Enter something you have memorized: ")
        Counter = Counter + 1
        return user_input


def written(user_input):
    ui = user_input
    with open("blackbox.txt", "w") as file:
        # Write the date and time above each record
        file.write(f"Difficulty {random_number} //{current_date_time}\n")
        file.write(f"Input {Counter}: {ui}\n")
        file.close()
        return file

while (counter != random_number):
     

Call = 
