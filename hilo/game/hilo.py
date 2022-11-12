import random
"""The card is: 9
Higher or Lower? [h/l] l
Next card was: 5
Your score is: 400
Play again? [y/n]

"""
class Hilo:
    
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        
        
    def draw(self):
        value = 1
        for card in self.cards:
            self.cards.append([card])
        value = value + 1
        
        random.shuffle(self.cards)
        score = 300
        card1 = self.cards
        
        value = random.shuffle(self.cards)
        self.points = print(f"Your score is: {score}")
        print(f"The current card is {card1[0]}")

        card2 = self.cards
        print(f"Your score is: {score}")
        
        self.choice = input("higher or lower? ")
        
        card2 = self.cards
        print(f"The next card is {card2[0]}")
        
        if self.choice == "h" and card2[1] > card1[1]:
            score += 100
        elif self.choice =="l" and card2[1] < card1[1]:
            score += 100
        elif self.choice =="h" and card2[1] == card1[1]:
            self.score += 0
        elif self.choice =="l" and card2[1] == card1[1]:
            score += 0
        else:
            score -= 75
        card1 = card2