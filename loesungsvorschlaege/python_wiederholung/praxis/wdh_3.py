# Lösungen zu den Aufgaben aus Unterabschnitt 1.3

import random


def quadratzahl():
    zufallszahl = random.randint(1, 100)
    potenz = pow(zufallszahl, 2)
    print(f"Die Quadratzahl von {zufallszahl} lautet {potenz}.")


# Aufagbe 1
quadratzahl()
quadratzahl()
quadratzahl()
print()

# Aufagbe 2
import turtle as t

t.speed(0)


def quadrat():
    for i in range(4):
        t.fd(100)
        t.lt(90)


t.pencolor("red")
for i in range(6):
    quadrat()
    t.lt(60)

# Aufgabe 3
t.clear()
t.pu()
t.home()
t.pd()

import math


def dach():
    t.forward(100)
    t.lt(135)
    d = math.sqrt(2) * 100 * 0.5
    t.forward(d)
    t.lt(90)
    t.forward(d)
    t.lt(135)


def geschoss():
    for i in range(4):
        t.fd(100)
        t.rt(90)


def haus():
    zufallsfarbe = random.choice(["red", "green", "blue"])
    t.pencolor(zufallsfarbe)
    geschoss()
    dach()
    t.fd(100)


for i in range(3):
    haus()


# Lösungen zu den Aufgaben aus Unterabschnitt 1.5

# Aufgabe 1
# Die vorherige Funktionsdefinition wird durch diese Funktionsdefinition ersetzt!
# Die vorherigen Funktionsaufrufe bleiben gültig, da das Programm von oben nach unten ausgeführt wird und
# weiter oben diese Funktion noch nicht "existiert".
def quadratzahl(basis):
    potenz = pow(basis, 2)
    print(f"Die Quadratzahl von {basis} lautet {potenz}.")


# Zufallszahl nun ausserhalb erzeugen und als Argument übergeben
zufallszahl = random.randint(1, 100)
quadratzahl(zufallszahl)

# Aufgabe 2
t.clear()
t.pu()
t.home()
t.pd()


def quadrat(seitenlaenge, farbe):
    t.pencolor(farbe)
    for i in range(4):
        t.fd(seitenlaenge)
        t.lt(90)


for i in range(6):
    quadrat(seitenlaenge=150, farbe="blue")
    t.lt(60)

# Aufgabe 3
t.clear()
t.pu()
t.home()
t.pd()


def dach(laenge=100):
    t.forward(laenge)
    t.lt(135)
    d = math.sqrt(2) * laenge * 0.5
    t.forward(d)
    t.lt(90)
    t.forward(d)
    t.lt(135)


def geschoss(laenge=100):
    for i in range(4):
        t.fd(laenge)
        t.rt(90)


def haus(laenge=100, farben=["red", "green", "blue"]):
    zufallsfarbe = random.choice(farben)
    t.pencolor(zufallsfarbe)
    geschoss(laenge)
    dach(laenge)
    t.fd(laenge)


for i in range(3):
    haus()

t.clear()
t.pu()
t.home()
t.pd()

for i in range(3):
    haus(laenge=50, farben=["pink", "cornflowerblue", "sandybrown"])


# Aufgabe 4
# Rekursion: Eine Funktion ruft sich innerhalb der Funktion selbst auf (Zeile 155).
# Damit dies nicht "unendlich oft" passiert, braucht es eine bedingte Anweisung (if-else).

def fakultaet(x):
    if x == 1:
        return 1
    else:
        return x * fakultaet(x - 1)


n = 5
ergebnis = fakultaet(n)
print(f"Fakultät von {n} ergibt {ergebnis}.")

t.done()
