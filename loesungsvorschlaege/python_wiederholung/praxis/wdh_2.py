# Lösungen zu den Kurzaufgaben (Abschnitt 5)

# Aufgabe 1
ducktales = ["Tick", "Trick", "Track"]
print(ducktales)
print()

# Aufgabe 2
chaos = ["42", 42.0, 42]
print(f"Typ der Liste: {type(chaos)}")
print(f"Typ für das 1. Element in der Liste (Index 0): {type(chaos[0])}")
print(f"Typ für das 2. Element in der Liste (Index 0): {type(chaos[1])}")
print(f"Typ für das 3. Element in der Liste (Index 0): {type(chaos[2])}")
print()

# Aufgabe 3
a = [1, 2, 3]
print("Vektor a:")
print(a)
b = [4, 5, 6]
print("Vektor b:")
print(b)
skalarprodukt = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
print(f"Skalarprodukt von a und b: {skalarprodukt}")
print()

# Aufgabe 4
# Für jeden Spieler gibt es eine Liste mit zwei Elementen.
# Das Ranking besteht dann aus einer Liste mit 5 Elementen, wobei die Elemente Listen der Länge 2 sind.
atp_ranking = [["Djokovic", 12113], ["Medvedev", 10220], ["Nadal", 8270], ["Tsitsipas", 8000], ["Zverev", 7340]]
print(atp_ranking)  # Gibt die verschachtelte Liste aus.
print()

# Aufgabe 5
import random

zufallszahlen = random.sample(range(0, 100), 20)
print("Alle Zufallszahlen:")
print(zufallszahlen)
teil_a = zufallszahlen[:10]
print("Erster Teil:")
print(teil_a)
teil_b = zufallszahlen[10:]
print("Zweiter Teil:")
print(teil_b)
print("Summen:")
summe_a = sum(teil_a)
print(f"Summe 1. Teil: {summe_a}")
print(f"Summe 2. Teil: {sum(teil_b)}")
