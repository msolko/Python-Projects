###########################################################################
#                       The Tortoise vs the Hare                          #
#                                                                         #
#   Programmed by Maxwell Solko (09-8-2017)                               #
#   Class:  CS200                                                         #
#   Instructor:  Chris Harris                                             #
#                                                                         #
#   Description:  This is a simulation of the famed race between the      #
#                 tortoise and the hare.  User input will determine the   #
#                 outcome.                                                #
#                                                                         #
###########################################################################

# Initialise variables
time = 0
distanceLead = 0.0
distTort = 0.0
distHare = 0.0
sleepHare = False
wakeTimeHare = 0
sleepTimeHare = 0
napTimeHare = 0

raceDistance = float(input("Race distance in feet: "))
speedHareOG = float(input("Hare's speed: "))
speedTort = float(input("Tortoise's speed: "))
wakeTime = float(input("Time between naps (awake): "))
napTime = float(input("Nap duration: "))
speedHare = speedHareOG #necessary for switching from asleep to awake

print("based on the stats entered above: this race will take place.")
print("---------------------------------------------------------------------------")
print("          Tortoise                   Hare                                        ")
print("time      position    speed          position    speed          comments         ")

while (distanceLead<raceDistance):
    time += 1
    commentNum = 0
    distTort += speedTort
    if (sleepHare == True):
        napTimeHare += 1
        if (napTimeHare >= napTime):#nested if statement to change from asleep to awake
            sleepHare = False
            napTimeHare = 0
            speedHare = speedHareOG
            commentNum = 2
    else:
        distHare += speedHare
        wakeTimeHare +=1
        if (wakeTimeHare >= wakeTime):
            sleepHare = True
            wakeTimeHare = 0
            speedHare = 0
            commentNum = 1
        if (distTort > raceDistance): distTort = raceDistance#make ties a lot more possible
        if (distHare > raceDistance): distHare = raceDistance
        
    distanceLead = max(distTort, distHare)
    if (distanceLead >= raceDistance and distTort > distHare): commentNum = 3
    if (distanceLead >= raceDistance and distTort < distHare): commentNum = 4
    if (distanceLead >= raceDistance and distTort == distHare): commentNum = 5

    #based on what happened in the code, one of these comments will show up.  the more important one override the lesser ones
    if (commentNum == 0): comment = " " 
    elif (commentNum == 1): comment= "Hare's nap started"
    elif (commentNum == 2): comment = "Hare's nap ended"
    elif (commentNum == 3): comment = "Race finished, Tortoise wins!"
    elif (commentNum == 4): comment = "Race finished, Hare wins!"
    elif (commentNum == 5): comment = "Race finished, it's a tie!"

    print('%-10s' '%-12s' '%-15s' '%-12s' '%-15s' '%-30s' % (time, round(distTort,6), speedTort, round(distHare,6), speedHare, comment))
