import random
import turtle as t

import colorgram

# ____ColorExtractionCode____
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# print(rgb_colors)


tim = t.Turtle()
t.colormode(255)

extracted_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                    (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for step in range(10):
    tim.dot(20, random.choice(extracted_colors))
    tim.forward(50)


# tbh from here on out the rest of the project is super repetetive and im here to learn. i know how to do this and i know i can do it but
# im ending this project here to avoid redundency.... ONWARD AND FORWARD!!!!! :D


screen = t.Screen()
screen.exitonclick()
