
from turtle import  Turtle
class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode="r") as data:
            self.high_score = int (data.read())
        self.color("white")
        self.penup()
        self.goto(20, 265)
        self.updating_score()
        self.hideturtle()
    def updating_score(self):
        self.clear()
        self.write(f"Score: {self.score}  high score {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def high_score_func(self):
        if self.score > self.high_score:
          self.high_score = self.score
          with open("data.txt",mode="w") as data:
              data.write(f"{self.high_score}")
        self.score = 0
        self.updating_score()


    def counter_of_food(self):
        self.score +=1
        self.updating_score()
