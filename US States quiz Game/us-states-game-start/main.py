

import turtle
import pandas

correct = 0

screen = turtle.Screen()
screen.title(f"Guess states correct")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
#  Adding image to the screen


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        """
        data of those states which are not entered by list comprehension
        """
        missing_states = [state for state in states if state not in guessed_states]
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("Remaining_State")
        break

    if answer_state in states:

        guessed_states.append(answer_state)

    #    checking if the state the user write is present in state list or not
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
    #         Check whether answer state is present in state data and get hold of the row data
        t.goto(int(state_data.x), int(state_data.y))
    #         move our turtle to x and y coordinate of the particular row which is in state data
        t.write(state_data.state.item())
    #           .item returns first element of the row
    #          name of the state is printed on that location


"""
data of those states which are not entered
"""

# for state in guessed_states:
#     if state in states:
#         states.remove(state)
# #         remove the state from states list that the user has not guessed
#
# data = pandas.DataFrame(states)
# data.to_csv("Remaining_State.csv")