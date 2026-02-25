import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('light blue')
turtle_screen.title("Kaplumbağayı yakala")
FONT = ('Arial', 30, 'normal')
grid_size = 15
score = 0
game_over = False

turtles = turtle.Turtle()

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.goto(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def setup_turtles():
    turtles.shape("turtle")
    turtles.shapesize(2,2)
    turtles.color("green")
    turtles.penup()

    def hand_click(x,y):
        global score
        score += 1
        turtles.clear()
        score_turtle.write("Score: {}".format(score), move = False, align="center", font=FONT)
    turtles.onclick(hand_click)

def move_turtle_randomly():
    if not game_over:
        turtles.hideturtle()

        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtles.goto(x, y)
        turtles.showturtle()
        turtle_screen.ontimer(move_turtle_randomly, 500)#x milisaniyede bir hareket etsin

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.goto(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        turtle_screen.ontimer(lambda: countdown(time - 1 ), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        turtles.hideturtle()
        countdown_turtle.write(arg="Game Over! :(", move=False, align="center", font=FONT)



def start_game_up():
    turtle.tracer(0)#takip etmeyi bırak
    setup_score_turtle()
    setup_turtles()
    move_turtle_randomly()
    countdown(25)
    turtle.tracer(1)#takip etmeyi başlat

start_game_up()
turtle.mainloop()