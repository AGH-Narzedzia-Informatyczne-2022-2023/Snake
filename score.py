class Score:
    def __init__(self):
        self.bestScore = 0
        self.currentScore = 0
    
    def incrementScore(self, amount):
        self.currentScore += amount
    
    def reset(self):
        if self.currentScore > self.bestScore:
            self.bestScore = self.currentScore
            self.currentScore = 0
