# 01_not_blank
def not_blank(question):
    while True:  # loops indefinitely until an acceptable input is received
        answer = input(question).strip()  # saves the input to "answer" variable, strips whitespace at the start or end of input

        if answer == "":  # checks if the answer is blank
            print("Input cannot be blank.")  # prints an error based on what has one wrong
        else:
            return answer  # returns the answer


# 02_get_input
def seat_counter():
    available_seats = 150  # declares the number of available seats
    while available_seats > 0:  # while loops the code when the available seats is more than 0
        print('There are {} seats remaining'.format(available_seats))  # prints the total number of remaining seats
        name = not_blank("What is your name?: ")  # uses the not_blank function so name is not blank
        available_seats -= 1  # reduces available seats by one each time
        print("Hello {}".format(name))  # prints greets user as a sign that the name has been accepted.
        age_check()


def age_check():
    while True:  # loops until break
        try:
            age = int(input("How old are you? "))
        except ValueError:  # confirms age is an integer
            print("Please input a whole number")
            continue  # restarts the loop
        if age < 12:  # if/elif/else for age logic
            print("You are too young to view the movie")
        elif age > 113:
            print("This age is fake, try again")
        else:
            print("Welcome")
            break  # exits the while loop as input was accepted

seat_counter()
