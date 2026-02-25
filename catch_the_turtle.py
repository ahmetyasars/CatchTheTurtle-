import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('light blue')
turtle_screen.title("Kaplumbağayı yakala")
FONT = ('Arial', 30, 'normal')
grid_size = 15
score = 0
game_over = False

#turtle list
turtle_list = []

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

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color('green')
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10 ,20]
y_coordinates = [-20, -10, 0, 10 ,20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list: #kaplumbağaları gizle
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()#öncekini gizle
        random.choice(turtle_list).showturtle()
        turtle_screen.ontimer(show_turtles_randomly, 350) #saniyede bir kaplumbağanın yeri değişsin

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
        hide_turtles()
        countdown_turtle.write(arg="Game Over! :(", move=False, align="center", font=FONT)



def start_game_up():
    turtle.tracer(0)#takip etmeyi bırak
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(25)
    turtle.tracer(1)#takip etmeyi başlat

start_game_up()
turtle.mainloop()