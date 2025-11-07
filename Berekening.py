

print("1: hoeveel is 13% van 365?")             
print("2: hoeveel procent is 121 van 412?")
print("3: 576 neemt toe met 17%; hoeveel heb je nu?")
print("4: 576 neemt af met 17%; hoeveel heb je nu?")


sommen = int(input("Welke vraag wil je gaan maken?: 1"))

def vraag1():
    antwoord = int(input("Vul je antwoord in"))
    ans1 = 27

    if antwoord == ans1:
        print("jouw antwoord is juist")
    elif antwoord != ans1:
        print("Jouw antwoord is onjuist probeer het opnieuw")
        vraag1()

 
def vraag2():
    antwoord = int(input("Vul je antwoord in"))
    ans2 = 29

    if antwoord == ans2:
        print("jouw antwoord is juist")
    elif antwoord != ans2:
        print("Jouw antwoord is onjuist proveer het opnieuw")
        vraag2()
def vraag3():
    antwoord = float(input("Vul hier procent getal in"))
    getal = 576
    ans3 = 673.92
    berekening = float(antwoord) * int(getal)
    if berekening == ans3:
        print("jouw antwoord is juist")
    elif berekening != ans3:
        print("Jouw antwoord is onjuist proveer het opnieuw")
        vraag3()
def vraag4():
    antwoord = float(input("Vul hier procent getal in"))
    getal = 576
    ans4 = 478.08
    berekening = float(antwoord) * int(getal)
    if berekening == ans4:
        print("jouw antwoord is juist")
    elif berekening != ans4:
        print("Jouw antwoord is onjuist probeer het opnieuw")
        vraag4()       



if sommen == 1:
    vraag1()
elif sommen == 2:
    vraag2()
elif sommen == 3:
    vraag3() 
elif sommen == 4:
    vraag4()       
    



   
   


   
