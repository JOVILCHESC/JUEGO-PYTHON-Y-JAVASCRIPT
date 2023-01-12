from juegolucha import *

def main():
    
    warrior1 = Warrior("Goro",random.randint(1000, 1500),random.randint(210, 250),random.randint(110, 130))
    mage1 = Mage("Terry",random.randint(1000, 1500),random.randint(210, 250),random.randint(110, 130))
    god1 = God("Midas",random.randint(1000, 1500),random.randint(210, 250),random.randint(110, 130))
    spartan1= Spartan("Fenrir",random.randint(1000, 1500),random.randint(210, 250),random.randint(110, 130))

    print("\nSelecciones 2 personajes para pelear")
    
    x=1
    print(f"\n{x}. {warrior1.name} ")

    x=2
    print(f"\n{x}. {mage1.name}")

    x=3
    print(f"\n{x}. {god1.name}") 

    x=4
    print(f"\n{x}. {spartan1.name}")

    option1=int(input("\nPlayer1: "))

    if option1==1:
        x=1
        warrior1.showcase(x)
        player1=warrior1

    elif option1==2:
        x=2
        mage1.showcase(x)
        player1=mage1

    elif option1==3:
        x=3
        god1.showcase(x)
        player1=god1
    
    elif option1==4:
        x=4
        spartan1.showcase(x)
        player1=spartan1

    else:
        "incorrecto"
    
    option2=int(input("\nPlayer2: "))

    if option2==1:
        x=1
        warrior1.showcase(x)
        player2=warrior1

    elif option2==2:
        x=2
        mage1.showcase(x)
        player2=mage1

    elif option2==3:
        x=3
        god1.showcase(x)
        player2=god1
    
    elif option2==4:
        x=4
        spartan1.showcase(x)
        player2=spartan1

    else:
        "incorrecto"

    player1.combat(player2)

    

if __name__ == "__main__":
    main()
