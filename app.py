from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from instrumentation import full, reduced, categorical

# App creation
app = Flask(__name__)
app.secret_key = "2791Gaston$"
Bootstrap(app)


# Home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Submit button was clicked
    if request.method == "POST":

        # Get form data
        number = request.form.get('number')
        instrumentation = request.form.get('type')

        # Full Instrumentation was selected
        if instrumentation == 'full':

            # Run the calculations
            result = full(int(number))

            # Formatting output
            flutes = "Flutes: " + str(result[0])
            oboes = "Oboes: " + str(result[1])
            bassoons = "Bassoons: " + str(result[2])
            clarinets = "Clarinets: " + str(result[3])
            bass_clarinets = "Bass Clarinets: " + str(result[4])
            alto_saxes = "Alto Saxes: " + str(result[5])
            tenor_saxes = "Tenor Saxes: " + str(result[6])
            bari_saxes = "Bari Saxes: " + str(result[7])
            trumpets = "Trumpets: " + str(result[8])
            french_horns = "French Horns: " + str(result[9])
            trombones = "Trombones: " + str(result[10])
            euphoniums = "Euphoniums: " + str(result[11])
            tubas = "Tubas: " + str(result[12])
            percussion = "Percussion: " + str(result[13])
            total = "Total: " + str(sum(result))

            # Output
            flash("<strong>Full Instrumentation</strong>")
            flash(flutes)
            flash(oboes)
            flash(bassoons)
            flash(clarinets)
            flash(bass_clarinets)
            flash(alto_saxes)
            flash(tenor_saxes)
            flash(bari_saxes)
            flash(trumpets)
            flash(french_horns)
            flash(trombones)
            flash(euphoniums)
            flash(tubas)
            flash(percussion)
            flash(total)

        # Reduced Instrumentation was selected
        elif instrumentation == 'reduced':

            # Run the calculations
            result = reduced(int(number))

            # Formatting output
            flutes = "Flutes: " + str(result[0])
            clarinets = "Clarinets: " + str(result[1])
            alto_saxes = "Alto Saxes: " + str(result[2])
            trumpets = "Trumpets: " + str(result[3])
            trombones = "Trombones: " + str(result[4])
            euphoniums = "Euphoniums: " + str(result[5])
            percussion = "Percussion: " + str(result[6])
            total = "Total: " + str(sum(result))

            # Output
            flash("<strong>Reduced Instrumentation</strong>")
            flash(flutes)
            flash(clarinets)
            flash(alto_saxes)
            flash(trumpets)
            flash(trombones)
            flash(euphoniums)
            flash(percussion)
            flash(total)

        # Categorical Instrumentation was selected
        elif instrumentation == 'category':

            # Run the calculations
            result = categorical(int(number))

            # Formatting output
            flutes = "Flutes: " + str(result[0])
            single_reeds = "Single Reeds: " + str(result[1])
            high_brass = "High Brass: " + str(result[2])
            low_brass = "Low Brass: " + str(result[3])
            percussion = "Percussion: " + str(result[4])
            total = "Total: " + str(sum(result))

            # Output
            flash("<strong>Categorical Instrumentation</strong>")
            flash(flutes)
            flash(single_reeds)
            flash(high_brass)
            flash(low_brass)
            flash(percussion)
            flash(total)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)