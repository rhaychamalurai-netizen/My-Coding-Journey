#This program recommends a simple day out based on the user's budget, avaiable hours, weathher and preferred vibe.

def main():
    funds = float(input("How much money do you have?"))
    hours = int(input("How much time do you have for this trip in hours?"))
    weather = input("Which weather do you prefer?")
    vibe = input("What's your preferred vibe? (nature, food, culture?)")
    suggestion = recommended (funds, hours, weather, vibe)
    print(suggestion)

def recommended (funds, hours, weather, vibe):
    if funds > 100 and hours > 12:
        print("Road Trip")
    elif funds > 80 and hours > 6:
        print ("Beach")
    elif funds > 60 and hours > 3:
        print("Restraunt")
    else:
        print ("Save up and come back next time :)")
   
    match weather, vibe:
        case "sunny" , "nature":
            return "Road trip or beach"
        case "Cloudy"| "rainy" | "rainy", "food" | "culture":
            return("restraunt")
        case _:
            return("Your funds and weather do not allow for this")
     
    return()

main()


    

    


