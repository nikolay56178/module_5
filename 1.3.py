import random
from random import randint 

class Warrior:
    def __init__(self,name):
      self.name = name
      self.health = 100
      self.damage = 20
      self.endurance = 100
      self.guard = 100

    def guarding(self):
      self.guard -= 20
      

    def hit(self,person):

      if person.health > 0:

        person.health -= self.damage
        self.endurance -= 10
        print(f'''{self.name} атакует {person.name}
Уровень здоровья {person.name} : {person.health}
Выносливость {self.name} : {self.endurance}
        ''')
        person.guarding()
      else:
        print(f'{person.name} Dead')



person1 = Warrior('Bambolbe')
person2 = Warrior('SpiderMan')

units = [person1, person2] 
 
while True: 
    idx = randint(0, 1) 
    attacks, opponent = units[idx], units[idx - 1] 
    attacks.hit(opponent) 
    if opponent.health <= 0:
        print(f'''{opponent.name} Dead...
          
{attacks.name} Win!
          ''')  
        break