import turtle as t
size = []

num = 0
while num == 0:
    h_of_t = input("input height:")
    if str.isdecimal(h_of_t) == True:
        h_of_t = int(h_of_t)
        num = 1
    else:
        print("you need to type in numbers")
size.append(h_of_t)

num = 0
while num == 0:
    w_of_t = input("input height:")
    if str.isdecimal(w_of_t) == True:
        w_of_t = int(w_of_t)
        num = 1
    else:
        print("you need to type in numbers")
size.append(w_of_t)
s = t.getscreen()
a = t.Turtle()