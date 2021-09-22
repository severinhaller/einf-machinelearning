import felder

class Spielbrett:
    def __init__(self):
        self.felder = [
            felder.Feld("Start"),
            felder.Feld("Dübendorfstrasse"),
            felder.Feld("Winterthurerstrasse"),
            felder.Feld("Schwammendingerplatz"),
            felder.Feld("Einkommenssteuer"),
            felder.Feld("Schwammendingerplatz"),
            felder.Feld("Gefängnis"),
            felder.Feld("Josefswiese"),
            felder.Feld("Escher-Wyss-Platz"),
            felder.Feld("Chance"),
            felder.Feld("Langstrasse"),
            felder.Feld("Freies Parken"),
            felder.Feld("Schaffhauserplatz"),
            felder.Feld("Universtitätstrasse"),
            felder.Feld("Irchelpark"),
            felder.Feld("Gehe ins Gefängnis"),
            felder.Feld("Bellevue"),
            felder.Feld("Niederdorf"),
            felder.Feld("Bahnhofstrasse"),
        ]