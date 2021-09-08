import main

crew_mitglied_1 = main.CrewMitglied()
crew_mitglied_1.nachname = "Quirk"
print(crew_mitglied_1.nachname)

crew_mitglied_4 = main.CrewMitglied()
crew_mitglied_4.nachname = "Quirky"
print(crew_mitglied_4.nachname)
print(main.CrewMitglied)
print(id(crew_mitglied_4.nachname))
print(crew_mitglied_4==crew_mitglied_1)


