import random
"""The card is: 9
Higher or Lower? [h/l] l
Next card was: 5
Your score is: 400
Play again? [y/n]

"""
class Hilo:
    
    def __init__(self):
        self.cards = 0
        self.score = 0
        
        
        
    def draw(self):
        self.cards = random.randint(1, 13)
        self.points = self.cards + 1
        
        score = 300
        card = self.cards
        
        self.points = print(f"Your score is: {score}")
        print(f"The current card is {card}")
        
        self.choice = input("Is the next card higher or lower? ")
        
        print(f"The next card is {card}")
        
        if self.choice == "h" and card > card:
            print("It is higher")
            print(f"Your score is: {score}")
            score += 100
        elif self.choice =="l" and card < card:
            print("It is lower")
            print(f"Your score is: {score}")
            score += 100
        elif self.choice =="h" and card == card:
            print("It was lower.")
            print(f"Your score is: {score}")
            self.score += -100
        elif self.choice =="l" and card == card:
            print("It was higher")
            print(f"Your score is: {score}")
            score += -100
        else:
            score -= 75
        card = card