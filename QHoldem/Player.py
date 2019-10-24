class Player:

    def __init__(self):
        self.wallet = 100
        self.points = 0
        self.rounds = 0

    def bet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount

    def win(self, amount):
        self.points += amount
        self.rounds += 1
        
    def broke(self):
        return self.wallet < 5
