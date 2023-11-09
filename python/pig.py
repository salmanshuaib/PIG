import random
import datetime

# isolate first digit after decimal point; in a number
def crown(princes):
    num_str = str(princes)
    decimal_index = num_str.find('.')
    if decimal_index != -1 and decimal_index + 1 < len(num_str):
        return int(num_str[decimal_index + 1])
    else:
        return None

# Function to get the current date and time as a string
def current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random number from 1 to 9
princes = random.uniform(0.1, 1)
emperor = 1
kings = (crown(princes))/10

princnes = 10
print(kings)

# Admission: Either BS can be returned for BS [OR] Surrender can be returned for BS. Pick one, Salman SHUAIB.
def Constancy(pilots):
    BitchSlap = input("Enter something you have memorized: ")
    pilots = pilots + 1
    return BitchSlap

def written(Xfile, ans):
    TotalKnockout = Xfile
    MerciBeaucoup = ans
    # Write the date and time above each record
    TotalKnockout.write(f"Difficulty {kings} //{current_date_time()}\n")  # Fixed the call to current_date_time()
    TotalKnockout.write(f"Input {princes}: {MerciBeaucoup}\n")
    return TotalKnockout


Xfile = open("blackbox.txt", "w")
while kings != emperor:
    y = Constancy(princes)
    thatsY = Xfile
    written(thatsY, y)
    kings = kings + 0.1

Xfile.close()