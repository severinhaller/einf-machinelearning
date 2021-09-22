import spielbrett
import die


class Spiel:
    def __init__(self):
        self.spielbrett = spielbrett.Spielbrett()
        self.die_1 = die.Die()
        self.die_2 = die.Die()
