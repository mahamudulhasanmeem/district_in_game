import turtle
import pandas

screen = turtle.Screen()
screen.title("BD District Map Location")
image = "PngItem_5237914.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("location.csv")
all_district = data.district.to_list()
guessed_district = []

while len(guessed_district) < 64:
    answer_user_district = screen.textinput(title=f"{len(guessed_district)}/64 District correct",
                                            prompt="next district").title()
    if answer_user_district == 'Exit':
        missing_list = []
        for district in all_district:
            if district not in guessed_district:
                missing_list.append(district)
        data_missing = pandas.DataFrame(missing_list)
        data_missing.to_csv("missing_district.csv")
        break

    if answer_user_district in all_district:
        guessed_district.append(answer_user_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_user_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer_user_district)














