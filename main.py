import time, os

if (os.name == "posix"):
    import replit

# to clear the screen I made a function
clear = lambda: os.system("cls")
newPower = lambda: os.system("start powershell -verb runas")

def cls():
    if windows:
        clear()
    else:
        replit.clear()

windows = False

#print(os.name)
if(os.name == "nt"):
    windows = True

# wait 1 sec
time.sleep(1)

cls()

# ask the user
print("Hva er ditt navn?")
# store the input in name
name = input()

# clear screen again
#clear()
cls()

# print a welcome message
print("Hello " +name + "!")

# spør om alder
print("Hvor gammel er du?")
age = int(input())

cls()

print("Har du hatt bursdag iår? (j/n)")
answer = input() # 49

if(answer == "n"): # I will be 50 years this spring, but I am only 49 now
    age += 1 # 50

# getting this year
yearNow = int(time.strftime("%Y")) # 2020

# how many year til I am 100 years old
diffToHundred = 100 - age # 100 - 50 = 50

# in what year will I be 100 years old
yearWhenHundred = yearNow + diffToHundred # 2020 + 50


cls()

# print it to the console
print("Du blir hundre år i " + str(yearWhenHundred) + ".")

print("Takk for at du tok deg tid til å finne dette ut og nå stenger jeg snart dette vinduet.")

if(os.name == "nt"):
    print("You're on a windows machine")
    newPower()
elif(os.name == "posix"):
    print("You're on a mac machine")
else:
    print("I don't know what system you're on. Sorry!")

