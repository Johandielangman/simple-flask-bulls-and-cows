from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = 'super secret'
DIGIT_LENGTH = 4
NUM_GUESSES = 6


@app.route("/", methods=["GET", "POST"])
def bulls_and_cows():
    feedback = None
    if "secret" not in session:
        session["secret"] = random.sample(range(1, 10), DIGIT_LENGTH)
        session["guess_number"] = 1
        session["history"] = []
        session["state"] = "playing"
        session["last_guess"] = ""

    if request.method == "POST":
        if session["state"] != "playing":
            return render_template(
                "index.html",
                feedback="Please reset the game",
                history=session["history"]
            )
        form_values = request.form.to_dict()
        session["last_guess"] = form_values['guess']
        session["guess_list"] = [int(c) for c in list(session["last_guess"])]
        if len(session["guess_list"]) != DIGIT_LENGTH:
            feedback = f"⚠ Your guess needs to be {DIGIT_LENGTH} long!⚠"
        else:
            bull_count = 0
            cow_count = 0
            for i, guess_digit in enumerate(session["guess_list"]):
                # ====> BULL IF CORRECT DIGIT AND CORRECT POSITION
                if guess_digit == session["secret"][i]:
                    bull_count += 1
                    continue
                # ====> ELSE, IF THE DIGIT IS CORRECT, BUT WRONG POSITION, THEN IT IS A COW
                if guess_digit in session["secret"]:
                    cow_count += 1

            # ====> CHECK IF WE WON THE GAME, ELSE GIVE FEEDBACK!
            if bull_count == DIGIT_LENGTH:
                session["state"] = "game over"
                return render_template(
                    "index.html",
                    feedback="You won!!! Have a croissant 🥐",
                    history=session["history"],
                    last_guess=session["last_guess"]
                )
            else:
                session["history"].append(f" {session['last_guess']} ➡ {bull_count} Bulls 🐂 | {cow_count} Cows 🐄")

            # ====> END THE GAME IF WE GUESS TOO MUCH!
            if session["guess_number"] == NUM_GUESSES:
                session["state"] = "game over"
                return render_template(
                    "index.html",
                    feedback=f"Game over AFTER {NUM_GUESSES} guesses. 🥕 Correct answer is {session['secret']}",
                    history=session["history"],
                    last_guess=session["last_guess"]
                )

            # ====> PREP FOR THE NEXT ROUND!
            session["guess_number"] += 1
    return render_template(
        "index.html",
        feedback=feedback,
        history=session["history"],
        last_guess=session["last_guess"]
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")  # Redirect to the game start
