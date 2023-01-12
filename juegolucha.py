import random
import time
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def attacke(self, other_character):
        #Genera un valor aleatorio para el daño entre el ataque -40 y el ataque del personaje + 40
        rdattack = random.randint(self.attack-40,self.attack+40)
        rddefense = random.randint(other_character.defense-30,other_character.defense+30)
        damage = rdattack - rddefense
        other_character.hp -= damage
        print(f"{self.name} lanza un ataque de {rdattack}")
        time.sleep(1)
        print(f"{other_character.name} se defendio con {rddefense}")
        time.sleep(1)
        print(f"{self.name} le hizo {damage} de daño a {other_character.name}!")
        time.sleep(2)
    

    def showcase(self, x):
        print(f"\n{x}. {self.name} | HP:  {self.hp} | RANGO DE ATAQUE: {self.attack-40}-{self.attack+40} | | RANGO DE DEFENSA: {self.defense-30}-{self.defense+30}")

    def life(self, vidainicial):

            print(f"\n{self.name}")
            porcent = (self.hp * 100)/vidainicial
            if self.hp == vidainicial:
                print(f"HP: {self.hp} ██████")
            elif (porcent)>=80:
                print(f"HP: {self.hp} █████")
            elif (porcent)>=60:
                print(f"HP: {self.hp} ████")
            elif (porcent)>=40:
                print(f"HP: {self.hp} ███")
            elif (porcent)>=20:
                print(f"HP: {self.hp} ██")
            else:
                print(f"HP: {self.hp} █")

    def combat(self, player2):
        i=0
        vida1=self.hp
        vida2=player2.hp
        input("\nPresione enter para pasar empezar")
        while self.hp > 0 and player2.hp > 0:

            i=i+1
            print("\n--------------------------------------------------------------------------------------------")
            print("\nMinuto", i)
            time.sleep(1)
            # Generamos un número aleatorio entre 0 y 1 para determinar si el ataque tiene éxito
            random_number = random.randint(0, 3)
            print(f"\n{self.name} Intenta atacar a {player2.name}")
            time.sleep(3)

            if random_number == 0:

                # Si el número es 0, entonces el ataque falla
                print(f"{self.name} fallo")
                time.sleep(2)
            else:
                # Si el número mayor a 0, entonces el ataque tiene éxito y se realiza el ataque
                self.attacke(player2)

            if player2.hp > 0:
                print(f"\n{player2.name} Coontraataca!\n")
                time.sleep(3)

                random_number2 = random.randint(0, 3)
                if random_number2 == 0:
                # Si el número es 0, entonces el ataque falla
                    print(f"{player2.name} fallo")
                    time.sleep(3)
                else:
                # Si el número es 1, entonces el ataque tiene éxito y se realiza el ataque
                    player2.attacke(self)


                if self.hp > 0 and player2.hp > 0:
                    print("\nResultados:")
                    time.sleep(1)
                    self.life(vida1)
                    time.sleep(1)
                    player2.life(vida2)
                    time.sleep(1)
                    input("\nPresione enter para pasar al siguiente round")
                
        
        if self.hp > 0:
            print(f"\n{self.name} GANOO!")
        else:
            print(f"\n{player2.name} GANOOO lol!")
        




class Warrior(Character):
    def _init_(self, name, hp, attack, defense):
        super()._init_(name, hp, attack, defense)

class Mage(Character):
    def _init_(self, name, hp, attack, defense):
        super()._init_(name, hp, attack, defense)

class God(Character):
    def _init_(self, name, hp, attack, defense):
        super()._init_(name, hp, attack, defense)

class Spartan(Character):
    def _init_(self, name, hp, attack, defense):
        super()._init_(name, hp, attack, defense)
        
