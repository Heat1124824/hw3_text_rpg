import os
from time import sleep
os.system("")

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
    def equip(self, weapon):
        self.weapon = weapon
    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name}對{target.name}使用{self.weapon.name}造成{self.weapon.damage}點傷害\n")
        print(f"{target.name}剩下{target.health}血\n")

class PlayerOne(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

class PlayerTwo(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

sword = Weapon("劍", 10)
bow = Weapon("弓", 6)
mage = Weapon("法器", 8)
fist = Weapon("拳頭", 2)

def weapon_choice(choice):
    if choice == "sword":
        return sword
    elif choice == "bow":
        return bow
    elif choice == "mage":
        return mage
    else:
        return fist

def main():
    round = 1
    playerOne = PlayerOne("Player 1", 30)
    playerTwo = PlayerTwo("Player 2", 30)

    while True:
        os.system("cls")
        print("HW3: 文字RPG")
        print("Round: ", round)
        print("Player 1 HP: ", playerOne.health, "Player 2 HP: ", playerTwo.health)

        choice_one = input("Player 1 請選擇武器(sword, bow, mage): ")
        attack_weapon = weapon_choice(choice_one)
        playerOne.equip(attack_weapon)
        playerOne.attack(playerTwo)
        if (playerTwo.health <= 0):
            print("Player 1贏了!")
            break
        sleep(1)
        choice_two = input("Player 2 請選擇武器(sword, bow, mage): ")
        attack_weapon = weapon_choice(choice_two)
        playerTwo.equip(attack_weapon)
        playerTwo.attack(playerOne)
        if (playerOne.health <= 0):
            print("Player 2贏了!")
            break
        sleep(1)
        round += 1

if __name__=="__main__": 
    main() 
    