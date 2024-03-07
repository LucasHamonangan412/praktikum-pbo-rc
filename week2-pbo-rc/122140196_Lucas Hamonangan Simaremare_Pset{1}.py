#122140196_Lucas Hamonangan Simaremare_Pset{1}

import random

class Parent:
    def __init__(self):
        self.blood_type = input("Enter the parent's allele: ").upper()

class Father(Parent):
    pass

class Mother(Parent):
    pass

class Child:
    def __init__(self, father, mother):
        self.allele = random.choice(father.blood_type) + random.choice(mother.blood_type)
        self.determine_blood_type()

    def determine_blood_type(self):
        blood_types = {
            'AA': 'A', 'AO': 'A', 'OA': 'A', 'OO': 'O',
            'BB': 'B', 'BO': 'B', 'OB': 'B',
            "AB": "AB", "BA": "AB"
        }
        
        self.blood_type = blood_types.get(self.allele, None)
        if not self.blood_type:
            print("Invalid allele combination.")
            return
        
        print(f"Child's allele: {self.allele}")
        print(f"Child's blood type: {self.blood_type}")

father = Father()
mother = Mother()
child = Child(father, mother)
