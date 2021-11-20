# Beispiel aus dem Skript in Python programmiert
# 3.2 Abstraktes Beispiel bzw. 3.3 Methode der kleinsten Quadrate

# Daten in einer Liste speichern
x_werte = [1, 2, 2.5]
y_werte = [1, 2, 1]
# Mittelwerte berechnen
avg_x = sum(x_werte) / 3
avg_y = sum(y_werte) / 3
# w_1 berechnen
# Summe im Zaehler
zaehler = (x_werte[0] - avg_x) * (y_werte[0] - avg_y) + (x_werte[1] - avg_x) * (y_werte[1] - avg_y) + (
        x_werte[2] - avg_x) * (y_werte[2] - avg_y)
# Summe im Nenner. Mit ** 2 wird potenziert mit dem Exponenten 2. Allgemein: basis ** exponent oder pow(basis, exponent)
nenner = (x_werte[0] - avg_x) ** 2 + (x_werte[1] - avg_x) ** 2 + (x_werte[2] - avg_x) ** 2
w_1 = zaehler / nenner
w_0 = avg_y - w_1 * avg_x
print(f"w_1: {w_1}")
print(f"w_0: {w_0}")
