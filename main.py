from replit import db
import random, time, os, datetime

print("My top secret diary 🔐")
    
def addEntry():
  newEntry = input("Dear diary... ")
  timestamp = datetime.datetime.now()
  db[timestamp] = newEntry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    nextEntry = input("Do you want to see the next entry? ")
    if nextEntry.lower()=="no":
      break

keys = db.keys()
if len(keys)<1:
  print("Welcome! Create your account")
  username = input("Username >")
  password = input("Password >") 
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword) 
  db[username] = {"password": newPassword, "salt": salt}
  print("User created!")
else:
  print("Welcome back! Log in")
  username = input("Username >")
  password = input("Password >") 
  if username not in keys:
    print("Incorrect username!")
    exit()
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  if db[username]["password"]==newPassword:
    print("Welcome!")
  else:
    print("Access denied!")
    
while True:
  menu = input("What would you like to do? \n1. Add entry \n2. View entries")
  if menu == "1":
    addEntry()
  if menu == "2":
    viewEntry()
