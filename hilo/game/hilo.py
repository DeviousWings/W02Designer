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
        card1 = self.cards
        
        self.points = print(f"Your score is: {score}")
        print(f"The current card is {card1}")

        card2 = self.cards
        print(f"Your score is: {score}")
        
        self.choice = input("higher or lower? ")
        
        card2 = self.cards
        print(f"The next card is {card2}")
        
        if self.choice == "h" and card2 > card1:
            score += 100
        elif self.choice =="l" and card2 < card1:
            score += 100
        elif self.choice =="h" and card2 == card1:
            self.score += 0
        elif self.choice =="l" and card2 == card1:
            score += 0
        else:
            score -= 75
        card1 = card2