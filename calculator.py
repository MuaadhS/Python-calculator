import re

prev_ans = 0
run = True

def  do_math():
    global run
    global prev_ans
    equation = ""
    if prev_ans == 0:
        equation = input("Enter a mathematical equation: ")
    else:
        equation = input (str(prev_ans))
    if equation == 'exit':
        print(" THANK YOU ")
        run = False
    else:
        equation = re.sub('[a-zA-Z,()" ":]', ' ', equation)
        if prev_ans == 0:
            prev_ans = eval(equation)
        else:
            prev_ans = eval(str(prev_ans) + equation)



print("Welcome To Python Calculator")
print("Type 'exit' to leave the program\n")

while run:
    do_math()