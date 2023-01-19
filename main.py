from flask import Flask, render_template
import random

app = Flask("Promillerechner")


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/hello')
def hello_world():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)


def calculate_bac():
    # Constants for alcohol density and metabolism rate
    # metabolism rate for men: 0.015; for women: 0.01
    # using 0.01 for simplicity
    m = 0.01
    weight = float(input("Bitte geben Sie ihr Gewicht in Kilogramm an. "))
    gender = input("Bitte geben Sie ihr Geschlecht an (m/w). ")
    if gender == "m":
        r = 0.68
    elif gender == "w":
        r = 0.55
    else:
        print("Ungültige Eingabe. Berechnungen werden standartisiert für das männliche Geschlecht durchgeführt.")
        r = 0.68
    bac = 0
    beer = float(input("Wie viele Liter Bier haben Sie konsumiert? (1 Flaschenbier = ~0.33l "))
    wine = float(input("Wie viele Liter Wein haben Sie konsumiert? (1 Glas Wein = ~0.185l "))
    cocktail = float(input("Wie viele Liter Cocktails oder Mischgetränke haben Sie konsumiert? (1 Cocktail = ~0.2l "))
    schnaps = float(input("Wie viele Liter harten Alkohol haben Sie konsumiert? (1 Shot = ~0.05l "))
    bac += (beer * 0.0514) / (weight * r)
    bac += (wine * 0.01269) / (weight * r)
    bac += (cocktail * 0.01800) / (weight * r)
    bac += (schnaps * 0.04000) / (weight * r)
    time_elapsed = int(input("Wie viel Zeit ist seit dem Start des Alkoholkonsums in Minuten vergangen? "))
    bac = bac * 100 - (m * (time_elapsed / 60))
    bac = round(bac, 2)
    if bac <= 0:
        print("Sie sind nüchtern.")
    else:
        sober_time = bac / m
        print(f"Ihr Blutalkoholgehalt ist: {bac}%")
        if beer > 0 and wine > 0 and cocktail > 0 and schnaps > 0:
            print("Durch Mischen verschiedenen Alkohols wird Ihr Kater deutlich spürbar sein.")
        elif bac < 0.2:
            print("Es ist mit einem leichten Kater zu rechnen.")
        elif bac < 0.5:
            print("Es ist mit einem mittelstarken Kater zu rechnen.")
        else:
            print("Es wird Ihnen Morgen furchtbar gehen.")
        print(f"Sie werden in ungefähr {sober_time:.2f} Stunden wieder nüchtern sein.")
        hangover_cures = ["Wasser trinken", "Schlafen", "Rohes Ei konsumieren", "Sport betreiben",
                          "Schmerzmittel konsumieren", "Kalt duschen", "Elektrolyte tanken (Gatorade etc.)",
                          "Kokosnusswasser trinken", "Tee trinken", "Massage machen lassen",
                          "Sich schwören nie mehr zu trinken", "Koffein vermeiden", "Nikotin vermeiden",
                          "Fettiges Essen vermeiden", "In der Dunkelheit bleiben", "Laute Geräusche vermeiden",
                          "Spazieren gehen", "ein Konterbier trinken", "LOTR-/Star Wars Marathon"]
        print("Eine bewährte Katerkur ist: " + random.choice(hangover_cures))
        if bac >= 0.5:
            print("In Ihrem Zustand ist es verboten Motorfahrzeuge und Fahrräder zu nutzen.")
        elif bac >= 0.2:
            print("Es ist nicht zu empfehlen in diesem Zustand ein Motorfahrzeug zu lenken.")
