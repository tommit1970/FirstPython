import time, replit

# to clear the screen I made a function
#import os
#clear = lambda: os.system("cls")
#clear()

#print(os.name)
replit.clear()

# wait 1 sec
time.sleep(1)

# ask the user
print("Hva er ditt navn?")
# store the input in name
name = input()

# clear screen again
#clear()
replit.clear()

# print a welcome message
print("Hello " +name + "!")

# spør om alder
print("Hvor gammel er du?")
age = int(input())

replit.clear()

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


replit.clear()

# print it to the console
print("Du blir hundre år i " + str(yearWhenHundred) + ".")

print("Takk for at du tok deg tid til å finne dette ut og nå stenger jeg snart dette vinduet.")



