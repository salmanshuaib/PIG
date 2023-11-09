import random
import datetime

# Function to get the current date and time as a string
def current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random number from 1 to 9
king = random.randint(1, 9)

pilots = 12
print(king)

# Admission: Either BS can be returned for BS [OR] Surrender can be returned for BS. Pick one, Salman SHUAIB.
def Constancy(pilots):
    BitchSlap = input("Enter something you have memorized: ")
    pilots = pilots + 1
    return BitchSlap

def written(Xfile, ans):
    TotalKnockout = Xfile
    MerciBeaucoup = ans
    # Write the date and time above each record
    TotalKnockout.write(f"Difficulty {king} //{current_date_time()}\n")  # Fixed the call to current_date_time()
    TotalKnockout.write(f"Input {pilots}: {MerciBeaucoup}\n")
    return TotalKnockout

emperor = 1
kings = 100
Xfile = open("blackbox.txt", "w")
while emperor != king:
    y = Constancy(pilots)
    thatsY = Xfile
    written(thatsY, y)
    emperor = kings + 1

Xfile.close()
