# Caclulate how many levels Nephi needs to obtain "x" many diamonds
# Calculate what Nephi can do to obtain "x" levels most effectivly
print("Welcome back Nephi!)
Option = input("how may I assist you today? (Diamonds/Levels): ")

#seperate Diamonds and Levels
if Option == "Diamonds":
 
  print("Diamonds selected.")
  
  DiamondInput = int(input("How many are you looking to obtain? "))
  if DiamondInput <= 100000:
    print("I see, a small goal...")
  elif DiamondInput <= 975000:
    print("Wonderful, a goal worth working towards!")
  elif DiamondInput >= 975001:
    print("Holy cheese sticks! WHAT DO YOU EVEN NEED THAT MANY FOR?!)
    print("I believe I will be needing more coffee before we continue...")
    print(". . .")
    print("okay, let's continue.")
          
  Gamepass = input("what gamepass do you own? (none/x2/x4/x6) ")
  if Gamepass == "x2":
  DiamondInput = DiamondInput *


  # WIP
  # Diamonds per level on line 13
  # 300dims no gamepass / 600dims x2 gamepass / 1200dims x4 gamepass / 1800dims both gamepasses

# Exp needed to level up: 325
# 240 exp from eating ( 0% - 100% )
# 200 exp from sleeping ( 0% - 100% )
# 150 exp from showering ( 0% - 100% )
