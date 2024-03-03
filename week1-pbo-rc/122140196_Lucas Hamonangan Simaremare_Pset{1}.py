#122140196_Lucas Hamonangan Simaremare_Pset{1}

class Character:
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense

    def attack(self, other):
        damage = max(0, 10 - other.defense)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        print(f"{other.name} now has {other.health} HP.")

def main():
    atreus = Character("Atreus", 500, 10)
    daedalus = Character("Daedalus", 750, 8)

    while True:
        print(f"\nRound-1 ====================================")
        print(f"{atreus.name}|{atreus.health}|{atreus.defense}|")
        print(f"{daedalus.name}|{daedalus.health}|{daedalus.defense}|\n")
        print("1. Attack     2. Defense     3. Give up")

        atreus_action = int(input(f"{atreus.name}, Select the action: "))
        daedalus_action = int(input(f"{daedalus.name}, Select the action: "))

        if atreus_action == 1:
            atreus.attack(daedalus)
        if daedalus_action == 1:
            daedalus.attack(atreus)
        if atreus_action == 3:
            print(f"{atreus.name} gives up!")
            print(f"{daedalus.name} wins!")
            break
        if daedalus_action == 3:
            print(f"{daedalus.name} gives up!")
            print(f"{atreus.name} wins!")
            break

        if atreus.health <= 0 or daedalus.health <= 0:
            print("\nGame Over!")
            if atreus.health <= 0:
                print(f"{daedalus.name} wins!")
            else:
                print(f"{atreus.name} wins!")
            break

if __name__ == "__main__":
    main()

