import turtle
import pandas as pd
IMG = './img/blank_states_img.gif'
DATA_DIR = './data/50_states.csv'

screen = turtle.Screen()
data = pd.read_csv(DATA_DIR)
states = data.state.to_list()
score = 0
guessed_states = []
end_game = False

screen.title('U.S. States Game')
turtle.addshape(IMG)
turtle.shape(IMG)

while score < 50 and not end_game:
    answer = str(screen.textinput(
        title=f'{score}/50 States Correct', prompt="Enter name of a state")).title()
    if answer == 'None' or answer == 'Exit':
        missing_states = list(set(states) - set(guessed_states))
        print(missing_states)
        end_game = True

    if answer in states and answer not in guessed_states:
        state_data = data[data.state == answer]

        score += 1
        guessed_states.append(answer)

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(state_data.x.item(), state_data.y.item())
        state.write(answer)

turtle.mainloop()
