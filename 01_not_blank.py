
def not_blank(question):
    while True:
        answer = input(question).strip()  # saves the input to "answer" variable, strips whitespace at the start or end of input

        if answer == "":  # checks if the answer is blank
            print("Input cannot be blank.")  # prints an error based on what has one wrong
        else:
            return answer  # returns the answer


name = not_blank("What is your name?: ")  # triggers not_blank with the input of question
print("Hello {}".format(name))  # greets user by printing the name
