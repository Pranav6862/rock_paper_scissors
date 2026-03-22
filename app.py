from flask import Flask, render_template, request
import random

app = Flask(__name__)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user = int(request.form["choice"])
        computer = random.randint(0, 2)

        user_choice = gestures[user]
        computer_choice = gestures[computer]

        if user == computer:
            result = "Draw!"
        elif (user == 0 and computer == 2) or \
             (user == 1 and computer == 0) or \
             (user == 2 and computer == 1):
            result = "You Win!"
        else:
            result = "You Lose!"

    return render_template("index.html",
                           result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)