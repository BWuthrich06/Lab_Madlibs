"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Say hello to user."""

    response = request.args.get("game_choice")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")
    



@app.route("/madlib")
def show_madlib():
    """"show madlib"""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    
    chosen_animals = []

    animal1 = request.args.get("animal1")
    animal2 = request.args.get("animal2")
    animal3 = request.args.get("animal3")
    animal4 = request.args.get("animal4")
    animal5 = request.args.get("animal5")

    animals=[animal1, animal2, animal3, animal4, animal5]

    for animal in animals:
        if animal:
            chosen_animals.append(animal)

    return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective, animals=chosen_animals)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
