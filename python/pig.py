import random
import datetime
from decimal import Decimal, getcontext
import string

# Set the precision for Decimal calculations
getcontext().prec = 10  # Adjust this value as needed

# Isolate first digit after decimal point in a number
def crown(princes):
    num_str = str(princes)
    decimal_index = num_str.find('.')
    if decimal_index != -1 and decimal_index + 1 < len(num_str):
        return (round(int(num_str[decimal_index + 1]))/10)
    else:
        return None

# Function to get the current date and time as a string
def current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random Decimal number from 0.1 to 1
princes = Decimal(random.uniform(0.1, 1))
king = Decimal(1)
sergeants = Decimal(crown(princes)) 

# Generate a random character from A to Z for the session
session_heading = random.choice(string.ascii_uppercase)

# Admission: Either BS can be returned for BS [OR] Surrender can be returned for BS.
def Constancy():
    BitchSlap = input("Enter something you have memorized: ")
    return BitchSlap

def written(Xfile, ans):
    TotalKnockout = Xfile
    MerciBeaucoup = ans
    TotalKnockout.write(f"Difficulty {princes} //{current_date_time()}\n")
    TotalKnockout.write(f"Input {princes}: {MerciBeaucoup}\n")
    return TotalKnockout

Xfile = open("blackbox.txt", "a")

paki = "\n"   #fyi: I am Pakistani; paki means bro to me, if you are offended, write your own program.
# Write the session heading once at the beginning of the session
Xfile.write(f"{paki}Session {session_heading} //{current_date_time()}\n")

while sergeants < king:
    y = Constancy()
    thatsY = Xfile
    written(thatsY, y)
    sergeants = sergeants + Decimal('0.1')  # Use Decimal for increment
    print(princes)
    print(king)
    print(sergeants) 

Xfile.close()
