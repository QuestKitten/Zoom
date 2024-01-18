# Caclulate how many levels *USER* needs to obtain "x" many diamonds
# Calculate what *USER* can do (shower/sleep/eat) & how many times each to obtain "x" levels most effectivly
User = input("Please enter your name: ")
print(f"Welcome back {User}")
Option = input("how may I assist you today? (Diamonds/Levels): ").lower()

#Defining variables
DiamondsFromLeveling = 300
ExperienceNeededPerLevel = 325




#seperate Diamonds and Levels

#Diamonds breakdown
if Option == "diamonds" :
    print("Diamonds selected.")


    while Option == "diamonds":
        
            DiamondInput = int(input("How many are you looking to obtain? (Please enter a whole number): "))
            if DiamondInput <= -1:
                print("What the hell are you doing?\nJust give away your diamonds you fool.")
                Diamonds = DiamondInput
                continue

            elif DiamondInput <= 100000:
                print("I see, a small goal...")
                Diamonds = DiamondInput
                break

            elif DiamondInput <= 975000:
                print("Wonderful, a goal worth working towards!")
                Diamonds = DiamondInput
                break

            elif DiamondInput >= 975001:
                print("Holy cheese sticks! WHAT DO YOU EVEN NEED THAT MANY FOR?! \nI believe I will be needing more coffee before we continue...\n. . .\nOkay, let's continue.")
                Diamonds = DiamondInput
                break

            #same as line 72 and line 110
            else:
                print("How did you manage to break the code this bad...")
                break
        

        #Loop in gamepass selection
    if Option == "diamonds":
        Gamepass = input("what gamepass do you own? (none/x2/x4/both): ")
        while Option == "diamonds":

            if Gamepass == "x2":
                DiamondsFromLeveling *= 2
                break

            elif Gamepass == "x4":
                DiamondsFromLeveling *= 4
                break

            elif Gamepass == "both":
                DiamondsFromLeveling *= 6
                break

            elif Gamepass == "none":
                DiamondsFromLeveling *= 1
                break
                
            #need to fix so it doesnt print infinite
            else:
                print("Please try again...")
                



        #Calculate number of levels
        LevelsNeeded = Diamonds // DiamondsFromLeveling

        #EXP per activity
        EXP_from_eating = 240
        EXP_from_sleeping = 200
        EXP_from_showering = 150

        #number of times to do each activity
        NumberTimesForEating = LevelsNeeded * ExperienceNeededPerLevel / EXP_from_eating
        NumberTimesForSleeping = LevelsNeeded * ExperienceNeededPerLevel / EXP_from_sleeping
        NumberTimesForShowering =LevelsNeeded * ExperienceNeededPerLevel / EXP_from_showering
        

        #Choice of action
        ActionChoice = input("Which way do you prefer to gain diamonds? (eat/sleep/bathe): ").lower()
        while Option == "diamonds":

            #need to make it go up to AT LEAST one level when diamonds are small (going to need to add in a level percent system)
            if ActionChoice == "eat":
                NumberOfFoodItemsNeeded = NumberTimesForEating * 4
                print(f"{User}, you would need to eat {round(NumberOfFoodItemsNeeded) + 1} food items.")
                break

            elif ActionChoice == "sleep":
                print(f"{User}, you would need to fill your energy bar, from 0% - 100%, {round(NumberTimesForSleeping) + 1} times.")
                break

            elif ActionChoice == "bathe":
                print(f"{User}, you would need to fill your hygiene bar, from 0%-100%, {round(NumberTimesForShowering) +1} times.")
                break
                
            #need to fix so it doesnt print infinite
            else:
                print("I don't understand your request, please try again.")




    #Levels breakdown
elif Option == "levels" or "level":
    print("Levels selected.")

    #while Option == "levels":






    #Failure breakdown
else:
    print("Try again or do us all a favour leave and never come back. <3")
