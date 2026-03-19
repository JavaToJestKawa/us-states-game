import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)

states = pandas.read_csv("50_states.csv").set_index("state").to_dict("index")
states_count = len(states)
score = 0

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

game_is_on = True


def draw_state_on_map(name, x, y):
    writer.goto(x, y)
    writer.write(name)
    print(writer)

while game_is_on and len(states) > 0:
    answer_state = screen.textinput(title=f"{score}/{states_count}", prompt="Guess the State")

    if answer_state.title() == "Exit":
        game_is_on = False

    states_keys = list(states.keys())
    for state_name in states_keys:
        if answer_state.title() == state_name.title():
            draw_state_on_map(state_name, states[state_name]["x"], states[state_name]["y"])
            states.pop(state_name)
            score += 1

with open("states_to_learn.csv", "w") as states_to_learn_file:
    states_to_learn_file.write(pandas.DataFrame(states.keys()).to_csv(index=False))
