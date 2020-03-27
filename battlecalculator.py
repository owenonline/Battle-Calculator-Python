import math
print("keep all values greater than 0")
forceA=float(input("Enter number of non artillery forces for side A: "))
forceB=float(input("Enter number of non artillery forces for side B: "))
deteffectivenessA=float(input("Enter the organic detection effectiveness (%) of side A: "))
deteffectivenessB=float(input("Enter the organic detection effectiveness (%) of side B: "))
deseffectivenessA =float(input("Enter the destruction effectiveness (%) of side A: "))
deseffectivenessB =float(input("Enter the destruction effectiveness (%) of side B: "))
encounterA =float(input("Enter the max number of side b's units side a can encounter (higher intelligence. set to 1 for none): "))
encounterB =float(input("Enter the max number of side a's units side b can encounter (higher intelligence. set to 1 for none): "))
capitulateA=float(input("Enter side a's capitulation percent: "))/100
capitulateB=float(input("Enter side b's capitulation percent: "))/100
combatA=deteffectivenessA*deseffectivenessA
combatB=deteffectivenessB*deseffectivenessB
remainingA=forceA
remainingB=forceB
t=0
linsqr=""
winner=""

def output(winner, remainingA, remainingB):
    if (winner=="b"):
        print("Winner: side ",winner,"\nRemaining units on Side A: ",remainingA,"\nRemaining units on side B: ",remainingB)
    else:
        print("A wins. Swap sides and run equation again to see casualty report")

if(encounterA==1and encounterB==1):
    if((combatB/combatA)>math.pow((forceA/forceB),2)):
        output("b",forceA*capitulateA,math.sqrt((combatA/combatB)*(math.pow(remainingA,2)-math.pow(forceA,2))+math.pow(forceB,2)))
    else:
        output("a",0,0)

elif(encounterA==1 and encounterB!=forceA and encounterB!=1):
    if(((combatB*encounterB)/combatA)>math.pow((forceA/forceB),2)):
         output("b",forceA*capitulateA,math.sqrt((combatA / (combatB*encounterB)) * (math.pow((forceA * capitulateA), 2) - math.pow(forceA, 2)) + math.pow(forceB, 2)))
    else:
        output("a",0,0)

elif(encounterA != 1 and encounterA != forceB and encounterB == 1):
    if((combatB / (combatA*encounterA)) > math.pow((forceA / forceB), 2)):
        output("b",forceA*capitulateA,math.sqrt(((combatA*encounterA) / combatB) * (math.pow((forceA * capitulateA), 2) - math.pow(forceA, 2)) + math.pow(forceB, 2)))
    else:
        output("a",0,0)

elif(encounterA == forceB and encounterB == forceA):
    if((combatB / combatA) > (forceA / forceB)):
        output("b",forceA*capitulateA,(combatA / combatB) * ((forceA * capitulateA) - forceA) + forceB)
    else:
        output("a",0,0)

elif(encounterA == forceB and encounterB != forceA and encounterB != 1):
    if(((combatB*encounterB) / combatA) > (math.pow(forceA,2) / forceB)):
        output("b",forceA*capitulateA,(combatA / (combatB*encounterB)) * (math.pow((forceA * capitulateA), 2) - math.pow(forceA, 2)) + forceB)
    else:
        output("a",0,0)

elif(encounterA != forceB and encounterA != 1 and encounterB == forceA):
    if((combatB / (combatA*encounterA)) > (forceA / math.pow(forceB,2))):
        output("b",forceA*capitulateA,math.sqrt(((combatA * encounterA) / combatB) * ((forceA * capitulateA) - forceA) + math.pow(forceB, 2)))
    else:
        output("a",0,0)

elif(encounterA==forceB and encounterB==1):
    if((combatB / combatA) > (math.pow(forceA, 2) / forceB)):
        output("b",forceA*capitulateA,(combatA / combatB) * (math.pow((forceA * capitulateA), 2) - math.pow(forceA, 2)) + forceB)
    else:
        output("a",0,0)

elif(encounterA == 1 and encounterB == forceA):
    if((combatB / combatA) > (forceA / math.pow(forceB, 2))):
        output("b",forceA*capitulateA,math.sqrt((combatA / combatB) * ((forceA * capitulateA) - forceA) + math.pow(forceB, 2)))
    else:
        output("a",0,0)