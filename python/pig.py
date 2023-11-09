import random
import datetime

# Function to get the current date and time as a string
def current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Generate a random number from 1 to 9
king = random.randint(1, 9)

pilot = 1
print(king)

def Constancy():
        BitchSlap = input("Enter something you have memorized: ")
        pilot = pilot + 1
        return BitchSlap

def written(Xfile, ans):
    TotalKnockout = Xfile
    MerciBeaucoup = ans
    # Write the date and time above each record
    TotalKnockout.write(f"Difficulty {king} //{current_date_time}\n")
    TotalKnockout.write(f"Input {pilot}: {MerciBeaucoup}\n")
    TotalKnockout.close()
    return TotalKnockout

emperor = 1
Xfile = open("blackbox.txt", "w")
while (emperor != king):
    y = Constancy()
    thatsY = Xfile
    written(thatsY, y)
    emperor = king + 1


Xfile.close()     

 
