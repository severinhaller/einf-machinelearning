# Lösungen zu den Kurzaufgaben (Abschnitt 3)

# Aufgabe 1
t1 = type(42)
print(f"Der Typ von 42 lautet: {t1}")
t2 = type(4.2)
print(f"Der Typ von 4.2 lautet: {t2}")
t3 = type("42")
print(f"Der Typ von \"42\" lautet: {t3}")
# Es gibt hier einen Fehler. Die Funktion type erwartet ein Argument (Übergabewert).
# Durch das Komma werden aber zwei Übergabewerte übermittelt.
# t4 = type(4,2)
# print(t4)
print()

# Aufgabe 2
x1 = "All"
x2 = "work"
x3 = "and"
x4 = "no"
x5 = "play"
x6 = "makes"
x7 = "Jack"
x8 = "a"
x9 = "dull"
x10 = "boy."
# Variablen durch Komma trennen
print(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
# f-String verwenden
print(f"{x1} {x2} {x3} {x4} {x5} {x6} {x7} {x8} {x9} {x10}")
print()

# Aufgabe 3
ergebnis_1 = 6 * 1 - 2
print(f"Ergebnis von 6 * 1 - 2: {ergebnis_1}")
# Klammern setzen, um die Reihenfolge der Berechnungen zu beeinflussen
ergebnis_2 = 6 * (1 - 2)
print(f"Ergebnis von 6 * (1 - 2): {ergebnis_2}")
print()

# Aufgabe 4
print("Variable bruce verwenden und 6 speichern.")
bruce = 6
ergebnis = bruce + 4
print(ergebnis)
print()

# Aufgabe 5
res = pow(2, 12)
print(f"Ergebnis von 2^12: {res}")
print(f"Typ des Ergebnis: {type(res)}")
print()

# Aufgabe 6
# Der "Plus-Operator" verhält sich anders, wenn man zwei Strings "addiert".
# Die beiden Strings werden nicht addiert (was auch nicht möglich ist), sondern
# zu einem (neuen) String verbunden (Fachbegriff: konkateniert eng. concatenate).
x1 = "apfel"
x2 = "baum"
x3 = x1 + x2
print(x3)
