from flask import Flask, render_template, request
import random

app = Flask("Promillerechner")

@app.route('/rechner', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        gender = request.form['gender']
        beer = float(request.form['beer'])
        wine = float(request.form['wine'])
        cocktail = float(request.form['cocktail'])
        schnaps = float(request.form['schnaps'])
        time_elapsed = int(request.form['time_elapsed'])

        def calculate_bac(weight, gender, beer, wine, cocktail, schnaps, time_elapsed):
            m = 0.1125
            if gender == "m":
                r = 0.68
            elif gender == "w":
                r = 0.55
            else:
                r = 0.68
            bac = 0
            bac += ((beer * 0.33) * 0.514) / (weight * r)
            bac += ((wine * 0.185) * 0.1269) / (weight * r)
            bac += ((cocktail * 0.2) * 0.1800) / (weight * r)
            bac += ((schnaps * 0.005) * 0.4000) / (weight * r)
            bac = bac * 100 - (0.1125 * (time_elapsed / 60))
            bac = round(bac, 2)
            return bac

        bac = calculate_bac(weight, gender, beer, wine, cocktail, schnaps, time_elapsed)
        if bac <= 0:
            result = ("Sie sind nüchtern.")
        else:
            sober_time = bac / 0.1125
            result = (f"Ihr Blutalkoholgehalt ist: {bac}%")
            if beer > 0 and wine > 0 and cocktail > 0 and schnaps > 0:
                result = ("Durch Mischen verschiedenen Alkohols wird Ihr Kater deutlich spürbar sein.")
            elif bac < 0.2:
                result = ("Es ist mit einem leichten Kater zu rechnen.")
            elif bac < 0.5:
                result = ("Es ist mit einem mittelstarken Kater zu rechnen.")
            else:
                result = ("Es wird Ihnen Morgen furchtbar gehen.")
            result = (f"Sie werden in ungefähr {sober_time:.2f} Stunden wieder nüchtern sein.")
            if bac >= 0.5:
                result = ("In Ihrem Zustand ist es verboten Motorfahrzeuge und Fahrräder zu nutzen.")
            elif bac >= 0.2:
                result = ("Es ist nicht zu empfehlen in diesem Zustand ein Motorfahrzeug zu lenken.")

        hangover_cures = ["Wasser trinken", "Schlafen", "Rohes Ei konsumieren", "Sport betreiben",
                          "Schmerzmittel konsumieren", "Kalt duschen", "Elektrolyte tanken (Gatorade etc.)",
                          "Kokosnusswasser trinken", "Tee trinken", "Massage machen lassen",
                          "Sich schwören nie mehr zu trinken", "Koffein vermeiden", "Nikotin vermeiden",
                          "Fettiges Essen vermeiden", "In der Dunkelheit bleiben", "Laute Geräusche vermeiden",
                          "Spazieren gehen", "ein Konterbier trinken", "LOTR-/Star Wars Marathon"]

        cures = random.sample(hangover_cures, 3)

        bac = calculate_bac(weight, gender, beer, wine, cocktail, schnaps, time_elapsed)
        return render_template('feedback.html', bac=bac, sober_time=bac / 0.1125, cure=cures)
    return render_template('formular.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
